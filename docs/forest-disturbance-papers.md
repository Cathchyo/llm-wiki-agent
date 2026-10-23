# 森林扰动论文存放与转换

## 放在哪里

新论文统一放在仓库根目录下的 `raw/papers/forest-disturbance/`。PDF 原文和转换后的 Markdown 成对存放，文件主名相同：

```text
raw/papers/forest-disturbance/
  2024-forest-disturbance-transformers.pdf
  2024-forest-disturbance-transformers.md
```

上面的文件名仅为示例。建议使用 `年份-英文短标题`，英文小写、单词之间用短横线，避免所有论文都叫 `main.pdf`。也可为每篇论文建立同名子目录，转换工具会递归处理。

既有论文保留原位置；新目录用于后续新增资料。

## 怎么转换

把 PDF 放进去后，可以直接告诉代理：

> 用 MarkItDown 转换 raw/papers/forest-disturbance/ 里的新论文，保留 PDF。

也可以在仓库根目录的 PowerShell 中运行：

```powershell
.\.venv\Scripts\python.exe -X utf8 tools/file_to_md.py --input_dir raw/papers/forest-disturbance
```

工具调用 MarkItDown，在 PDF 旁生成 UTF-8 编码的同名 `.md`，默认保留 PDF；已有同名 Markdown 会跳过，不覆盖。不要使用 `--delete_source`，以保留原文。

若重建 Python 环境，推荐按仓库根 README 使用 `uv sync --locked`。仅安装本 PDF 转换流程所需依赖时，可运行：

```powershell
.\.venv\Scripts\python.exe -m pip install "markitdown[pdf]>=0.1.5,<0.2.0" "tqdm>=4.67.3,<5.0.0"
```

## 转换后

转换完成后先检查 Markdown 是否完整、可读。多栏排版、公式、表格或扫描版 PDF 的提取结果可能需要核对原文。转换只准备原始资料；摘要在 `review/` 审核，用户逐步批准后才可进入 `wiki/`。
