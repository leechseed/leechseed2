import os
import subprocess

def convert_epubs_to_pdfs(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.epub'):
            epub_path = os.path.join(directory, filename)
            pdf_path = os.path.splitext(epub_path)[0] + ".pdf"
            cmd = [r'C:\Program Files\Calibre2\ebook-convert.exe', epub_path, pdf_path]

            print(f"Running command: {' '.join(cmd)}")

            try:
                subprocess.run(cmd, check=True)
                print(f"Converted {epub_path} to {pdf_path}")
            except subprocess.CalledProcessError as e:
                print(f"Conversion of {epub_path} failed with error:\n{e}")

# example usage:
directory = r"C:\Users\U01_LEECHSEED\Desktop\BOOKS\0.Unprocessed"
convert_epubs_to_pdfs(directory)
