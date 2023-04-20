# script to break prepared pdfs into block sizing dependent on text
def break_text_into_blocks(input_file, output_file, block_size=600):
    with open(input_file, 'r') as file:
        text = file.read()

    words = text.split()
    num_blocks = (len(words) + block_size - 1) // block_size

    with open(output_file, 'w') as output:
        for i in range(num_blocks):
            start = i * block_size
            end = min((i + 1) * block_size, len(words))
            block = ' '.join(words[start:end])
            output.write(block)
            output.write('\n\n')

input_txt = 'input.txt'
output_txt = 'output_blocks.txt'
break_text_into_blocks(input_txt, output_txt)
