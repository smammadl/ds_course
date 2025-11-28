# requires pandoc + miktex
# first test run to make sure convertion works, try:
# pandoc -s -V geometry:margin=1in .\filename.md -o .\filename.pdf

from pathlib import Path
import sys
import subprocess

current_dir = Path(__file__).parent
main_dir = current_dir.parent
pdf_dir = main_dir/'files/pdfs'
pdf_dir.mkdir(exist_ok=True, parents=True)

file_paths = list(main_dir.glob("[0-9].[0-9]*.md"))
file_paths = [p for p in file_paths if 'exercises' not in p.name]

for p in file_paths:
    md_path = p.resolve()
    pdf_name = p.with_suffix('.pdf').name
    pdf_path = pdf_dir / pdf_name
    print(pdf_path)
    subprocess.run(['pandoc', '-s', '-V', 'geometry:margin=1in', md_path, '-o', pdf_path])