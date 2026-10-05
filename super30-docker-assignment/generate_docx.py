import sys
from docx import Document

from pathlib import Path

def md_to_docx(md_path, docx_path):
    md = Path(md_path).read_text(encoding='utf-8')
    doc = Document()
    for line in md.splitlines():
        if line.strip().startswith('# '):
            doc.add_heading(line.strip().lstrip('# ').strip(), level=1)
        elif line.strip().startswith('## '):
            doc.add_heading(line.strip().lstrip('#').strip(), level=2)
        elif line.startswith('```'):
            # start/end code block; simple handling: collect until closing
            # naive: add the fenced block as a paragraph
            doc.add_paragraph(line)
        else:
            doc.add_paragraph(line)
    doc.save(docx_path)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python generate_docx.py input.md output.docx')
        sys.exit(1)
    md_to_docx(sys.argv[1], sys.argv[2])
