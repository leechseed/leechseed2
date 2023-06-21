import os
import argparse
from ebooklib import epub
from pdfdocument.document import PDFDocument

def epub_to_pdf(epub_path, pdf_path):
    book = epub.read_epub(epub_path)

    pdf = PDFDocument(pdf_path)
    pdf.init_report()

    for item in book.get_items():
        if isinstance(item, epub.EpubHtml):  # checking if item is a document
            content = item.get_content().decode('utf-8', errors='ignore')
            # remove HTML tags and blank lines
            content = os.linesep.join([s for s in content.splitlines() if s])
            pdf.h2(item.get_name())
            pdf.p(content)

    pdf.generate()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert EPUB to PDF.')
    parser.add_argument('epub', help='Path to the EPUB file')
    parser.add_argument('pdf', help='Path to the output PDF file')

    args = parser.parse_args()

    epub_to_pdf(args.epub, args.pdf)
