# script to break prepared pdfs into block sizing dependent on text
def pyblok(input_file, output_file, block_size=600):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    num_blocks = (len(words) + block_size - 1) // block_size

    with open(output_file, 'w', encoding='utf-8') as output:
        for i in range(num_blocks):
            start = i * block_size
            end = min((i + 1) * block_size, len(words))
            block = ' '.join(words[start:end])
            output.write(block)
            output.write('\n\n')

input_txt = '7.txt'
output_txt = '7blokd.txt'
pyblok(input_txt, output_txt)
