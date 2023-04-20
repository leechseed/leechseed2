# this script is the same as pyblok but does multiple files

multiblok(input_files, block_size=600):
    for input_file in input_files:
        output_file = input_file.replace('.txt', '_blocks.txt')

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

input_files = ['input1.txt', 'input2.txt', 'input3.txt']
break_text_into_blocks(input_files)
