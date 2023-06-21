#### this script is designed to remove hypens from line breaks within the text

import re

def remove_hyphenation(text):
    return re.sub(r'(\w)-\s+(\w)', r'\1\2', text)

# Read the input text file
input_file = '1raw-in.txt'
with open(input_file, 'r') as file:
    text = file.read()

# Remove hyphenations from the text
clean_text = remove_hyphenation(text)

# Write the processed text to an output file
output_file = '2outputt.txt'
with open(output_file, 'w') as file:
    file.write(clean_text)