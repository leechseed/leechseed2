# script used to turn pdfs into txts

import pdfplumber

def pybuk(input_file, output_file):
    with pdfplumber.open(input_file) as pdf:
        with open(output_file, 'w') as output:
            for page in pdf.pages:
                text = page.extract_text()
                output.write(text)

input_pdf = 'input.pdf'
output_txt = 'output.txt'
pybuk(input_pdf, output_txt)
