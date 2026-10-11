import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'tmp' / 'ccdc'
STAGING = Path(__file__).resolve().parent
DESTINATION = ROOT / 'raw' / 'ccdc_deep_learning'

JOBS = [
    dict(slug='ccdc', source='continuous change detection and classification.pdf',
         title='Continuous change detection and classification of land cover using all available Landsat data',
         date='2014-02-11', prefix='20140211', issue_year=2014, pages=20, doi='10.1016/j.rse.2014.01.011'),
    dict(slug='cold', source='Continuous monitoring of land disturbance based on Landsat time series.pdf',
         title='Continuous monitoring of land disturbance based on Landsat time series',
         date='2019-03-13', prefix='20190313', issue_year=2020, pages=18, doi='10.1016/j.rse.2019.03.009'),
    dict(slug='sccd', source='A near-real-time approach for monitoring forest disturbance using Landsat time series- Stochastic continuous change detection.pdf',
         title='A near-real-time approach for monitoring forest disturbance using Landsat time series: stochastic continuous change detection',
         date='2020-11-05', prefix='20201105', issue_year=2021, pages=17, doi='10.1016/j.rse.2020.112167'),
    dict(slug='land-change-review', source='Remote sensing of land change- A multifaceted perspective.pdf',
         title='Remote sensing of land change: A multifaceted perspective',
         date='2022-10-07', prefix='20221007', issue_year=2022, pages=20, doi='10.1016/j.rse.2022.113266'),
    dict(slug='ob-cold', source='Object-based continuous monitoring of land disturbances from dense Landsat time series.pdf',
         title='Object-based continuous monitoring of land disturbances from dense Landsat time series',
         date='2023-01-27', prefix='20230127', issue_year=2023, pages=15, doi='10.1016/j.rse.2023.113462'),
    dict(slug='leveraging', source='Leveraging past information and machine learning to accelerate land disturbance monitoring.pdf',
         title='Leveraging past information and machine learning to accelerate land disturbance monitoring',
         date='2024-05', prefix='202405', issue_year=2024, pages=15, doi='10.1016/j.rse.2024.114071'),
    dict(slug='forest-agents', source='Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset.pdf',
         title='Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset',
         date='2026-05-06', prefix='20260506', issue_year=2026, pages=16, doi='10.1016/j.rse.2026.115461'),
]


def compact(text):
    text = unicodedata.normalize('NFKC', text).casefold()
    return re.sub(r'\W+', '', text)


def checksum(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def windows_filename(text):
    replacements = {':': '：', '?': '？', '*': '＊', '"': '＂', '<': '＜', '>': '＞', '|': '｜', '/': '／', '\\': '＼'}
    return ''.join(replacements.get(character, character) for character in text).rstrip(' .')


sys.stdout.reconfigure(encoding='utf-8')
pdfs = {p.name for p in SOURCE.rglob('*') if p.is_file() and p.suffix.lower() == '.pdf'}
assert pdfs == {job['source'] for job in JOBS}, 'PDF inventory changed; review jobs before writing'
source_hashes = {job['source']: checksum(SOURCE / job['source']) for job in JOBS}
prepared = []
for job in JOBS:
    intermediate = STAGING / f"{job['slug']}.markitdown-0.1.5.md"
    body = intermediate.read_text(encoding='utf-8').strip()
    assert len(body) > 1000, f"Empty or short conversion: {job['source']}"
    assert '\ufffd' not in body, f"Replacement characters in: {job['source']}"
    assert 'references' in body.casefold(), f"Missing reference section: {job['source']}"
    assert compact(job['title']) in compact(body[:15000]), f"Title mismatch: {job['source']}"
    if job['slug'] == 'cold':
        assert 'corrigendum' in body.casefold(), 'Appended correction missing'
    filename = f"{job['prefix']}_{windows_filename(job['title'])}.md"
    target = DESTINATION / filename
    assert not target.exists(), f'Refusing to overwrite immutable source: {target}'
    metadata = {
        'title': job['title'],
        'publication_date': job['date'],
        'publication_date_precision': 'month' if job['slug'] == 'leveraging' else 'day',
        'publication_date_basis': 'journal_issue' if job['slug'] == 'leveraging' else 'first_online',
        'journal_issue_year': job['issue_year'],
        'doi': job['doi'],
        'source_pdf': (SOURCE / job['source']).relative_to(ROOT).as_posix(),
        'source_pdf_pages': job['pages'],
        'converter': 'MarkItDown 0.1.5 [pdf]',
    }
    if job['slug'] == 'leveraging':
        metadata['date_note'] = '原 PDF 未标注首次在线发表日期；采用 Crossref 登记的 2024 年 5 月刊期，具体日未知。'
        metadata['date_reference'] = 'https://api.crossref.org/works/10.1016%2Fj.rse.2024.114071'
    else:
        metadata['date_reference'] = '原 PDF 首页 Available online'
    if job['slug'] == 'cold':
        metadata['source_note'] = '原 PDF 包含主论文及末尾更正页；日期前缀采用主论文首次在线发表日期，更正页一并保留。'
    frontmatter = '\n'.join(f'{key}: {json.dumps(value, ensure_ascii=False)}' for key, value in metadata.items())
    output = f"---\n{frontmatter}\n---\n\n# {job['title']}\n\n{body}\n"
    prepared.append((job, target, output))

DESTINATION.mkdir(parents=True, exist_ok=True)
report = []
for job, target, output in prepared:
    with target.open('x', encoding='utf-8', newline='\n') as stream:
        stream.write(output)
    saved = target.read_text(encoding='utf-8')
    assert saved == output, f'Written content mismatch: {target}'
    report.append(dict(file=target.relative_to(ROOT).as_posix(), date=job['date'],
                       date_basis='journal_issue' if job['slug'] == 'leveraging' else 'first_online',
                       pages=job['pages'], bytes=target.stat().st_size,
                       source_pdf_sha256=source_hashes[job['source']]))
for source_name, before in source_hashes.items():
    assert checksum(SOURCE / source_name) == before, f'Source PDF modified: {source_name}'
(STAGING / 'conversion-manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'converted': len(report), 'source_pages': sum(job['pages'] for job in JOBS), 'files': report}, ensure_ascii=False, indent=2))
