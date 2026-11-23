from __future__ import annotations

import hashlib
import json
import re
from html import escape
from pathlib import Path

import pdfplumber
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / '农业工程与信息案例课程答辩-王圣杰-8分钟汇报稿.md'
OUTPUT = SOURCE.with_suffix('.pdf')
QA = ROOT / 'speech_pdf_qa'
QA.mkdir(exist_ok=True)

source_bytes = SOURCE.read_bytes()
markdown = source_bytes.decode('utf-8-sig')
pdfmetrics.registerFont(TTFont('SpeechBody', r'C:\Windows\Fonts\Deng.ttf'))
pdfmetrics.registerFont(TTFont('SpeechBold', r'C:\Windows\Fonts\Dengb.ttf'))
pdfmetrics.registerFontFamily('SpeechBody', normal='SpeechBody', bold='SpeechBold', italic='SpeechBody', boldItalic='SpeechBold')

navy = colors.HexColor('#203247')
styles = {
    'body': ParagraphStyle('Body', fontName='SpeechBody', fontSize=12, leading=21, textColor=colors.HexColor('#222222'), alignment=TA_LEFT, wordWrap='CJK', spaceAfter=10, allowWidows=0, allowOrphans=0),
    'h1': ParagraphStyle('Title', fontName='SpeechBold', fontSize=19, leading=28, textColor=navy, wordWrap='CJK', spaceAfter=12, keepWithNext=True),
    'h2': ParagraphStyle('Section', fontName='SpeechBold', fontSize=14, leading=22, textColor=navy, wordWrap='CJK', spaceBefore=12, spaceAfter=7, keepWithNext=True),
    'h3': ParagraphStyle('Subsection', fontName='SpeechBold', fontSize=12, leading=20, textColor=navy, wordWrap='CJK', spaceBefore=8, spaceAfter=6, keepWithNext=True),
    'subtitle': ParagraphStyle('Subtitle', fontName='SpeechBold', fontSize=11, leading=18, textColor=colors.HexColor('#666666'), spaceAfter=14, keepWithNext=True),
}


def inline(value: str) -> str:
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', escape(value))


story = []
for block in re.split(r'\n\s*\n', markdown.strip()):
    block = block.strip()
    if block == '## 五、实验结果':
        story.append(PageBreak())
    if block.startswith('### '):
        text, style = block[4:], styles['h3']
    elif block.startswith('## '):
        text, style = block[3:], styles['h2']
    elif block.startswith('# '):
        text, style = block[2:], styles['h1']
    elif block == '**8 分钟汇报稿**':
        text, style = block[2:-2], styles['subtitle']
    else:
        text, style = ' '.join(block.splitlines()), styles['body']
    story.append(Paragraph(inline(text), style))


def decorate(canvas, document):
    canvas.saveState()
    width, height = A4
    canvas.setFont('SpeechBody', 8)
    canvas.setFillColor(colors.HexColor('#777777'))
    canvas.drawString(48, height - 30, '森林扰动检测 | 汇报稿')
    canvas.setStrokeColor(colors.HexColor('#D6DCE2'))
    canvas.setLineWidth(0.4)
    canvas.line(48, 39, width - 48, 39)
    canvas.drawCentredString(width / 2, 24, f'第 {document.page} 页')
    canvas.restoreState()


doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=48, rightMargin=48, topMargin=49, bottomMargin=52, title='基于 Transformer 和 Sentinel-2 时间序列的森林扰动检测 - 汇报稿', author='', pageCompression=1)
doc.build(story, onFirstPage=decorate, onLaterPages=decorate)


def normalize(value: str) -> str:
    return re.sub(r'\s+', '', value)


expected = re.sub(r'^#{1,3}\s+', '', markdown, flags=re.M).replace('**', '')
page_stats = []
content = []
with pdfplumber.open(OUTPUT) as pdf:
    for index, page in enumerate(pdf.pages, start=1):
        text = page.extract_text() or ''
        body = '\n'.join(line for line in text.splitlines() if line != '森林扰动检测 | 汇报稿' and not re.fullmatch(r'第\s*\d+\s*页', line))
        content.append(body)
        chars = page.chars
        outside = [c for c in chars if c['x0'] < 40 or c['x1'] > page.width - 40 or c['top'] < 10 or c['bottom'] > page.height - 12]
        page_stats.append({'page': index, 'characters': len(body), 'out_of_bounds_characters': len(outside)})
        if outside:
            raise ValueError(f'Page {index} contains text outside margins')

actual = normalize(''.join(content))
wanted = normalize(expected)
if actual != wanted:
    limit = min(len(actual), len(wanted))
    mismatch = next((i for i in range(limit) if actual[i] != wanted[i]), limit)
    raise ValueError(f'Text mismatch at {mismatch}: actual={actual[mismatch:mismatch+60]!r}; expected={wanted[mismatch:mismatch+60]!r}')
if SOURCE.read_bytes() != source_bytes:
    raise ValueError('Markdown source changed during conversion')

document = pdfium.PdfDocument(str(OUTPUT))
thumbnails = []
for index in range(len(document)):
    page = document[index]
    bitmap = page.render(scale=1.5)
    preview = bitmap.to_pil().convert('RGB')
    preview.save(QA / f'page-{index + 1:02d}.png')
    preview.thumbnail((780, 1105))
    thumbnails.append(preview.copy())
    bitmap.close()
    page.close()
document.close()

columns = 2
cell_width, cell_height = 812, 1150
rows = (len(thumbnails) + columns - 1) // columns
sheet = Image.new('RGB', (columns * cell_width, rows * cell_height), '#DEE3E8')
draw = ImageDraw.Draw(sheet)
for index, preview in enumerate(thumbnails):
    x = (index % columns) * cell_width + 16
    y = (index // columns) * cell_height + 24
    sheet.paste(preview, (x, y))
    draw.text((x, y - 18), f'Page {index + 1}', fill='#26364A')
sheet.save(QA / 'contact-sheet.png')

report = {'output': str(OUTPUT), 'pages': len(thumbnails), 'bytes': OUTPUT.stat().st_size, 'source_sha256': hashlib.sha256(source_bytes).hexdigest(), 'text_matches_markdown': True, 'pages_checked': page_stats, 'preview': str(QA / 'contact-sheet.png')}
(QA / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False))
