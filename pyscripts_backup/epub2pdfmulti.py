import subprocess
import os

def convert_epubs_to_pdfs(epub_paths):
    for epub_path in epub_paths:
        pdf_path = os.path.splitext(epub_path)[0] + ".pdf"
        cmd = ['ebook-convert', epub_path, pdf_path]
        
        try:
            subprocess.run(cmd, check=True)
            print(f"Converted {epub_path} to {pdf_path}")
        except subprocess.CalledProcessError as e:
            print(f"Conversion of {epub_path} failed with error:\n{e}")

# example usage:
epub_paths = [
    r"C:\Users\U01_LEECHSEED\Desktop\BOOKS\EPUBS\01 - Never Deal with a Dragon - Robert N. Charrette.epub",
    r"C:\Users\U01_LEECHSEED\Desktop\BOOKS\EPUBS\02 - Choose Your Enemies Carefully - Robert N. Charrette.epub"
]
convert_epubs_to_pdfs(epub_paths)

