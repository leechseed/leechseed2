import subprocess
import os

def convert_epub_to_pdf(epub_path):
    pdf_path = os.path.splitext(epub_path)[0] + ".pdf"
    cmd = ['ebook-convert', epub_path, pdf_path]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Converted {epub_path} to {pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed with error:\n{e}")

# example usage:
epub_path = input("Please enter the path to your .epub file: ")
convert_epub_to_pdf(epub_path)
