import os
import subprocess

def convert_to_pdf(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.epub', '.mobi', '.azw3')):
            file_path = os.path.join(directory, filename)
            pdf_path = os.path.splitext(file_path)[0] + ".pdf"
            cmd = [r'C:\Program Files\Calibre2\ebook-convert.exe', file_path, pdf_path]

            print(f"Running command: {' '.join(cmd)}")

            try:
                subprocess.run(cmd, check=True)
                print(f"Converted {file_path} to {pdf_path}")
            except subprocess.CalledProcessError as e:
                print(f"Conversion of {file_path} failed with error:\n{e}")

# example usage:
directory = r"C:\Users\U01_LEECHSEED\Desktop\BOOKS\0.Unprocessed"
convert_to_pdf(directory)
