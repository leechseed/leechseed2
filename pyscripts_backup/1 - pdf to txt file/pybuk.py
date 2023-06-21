# script used to turn pdfs into txts

import pdfplumber

def pybuk(input_file, output_file):
    with pdfplumber.open(input_file) as pdf:
        with open(output_file, 'w', encoding='utf-8') as output:
            for page in pdf.pages:
                text = page.extract_text()
                output.write(text)

input_pdf = '9781405859141buk.pdf'
output_txt = 'output9781405859141buk.txt'
pybuk(input_pdf, output_txt)
