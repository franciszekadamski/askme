#!/usr/bin/python3

with open('spanish_1000.txt', 'r') as f:
   lines = f.readlines()
   f.close()

part_n = 1
new_content = ''
for n, line in enumerate(lines):
    line = line.replace(' ', '')
    line_content = line.split('\t')

    spanish_word = line_content[1]
    english_word = line_content[2]

    new_content += spanish_word  + '\n'
    new_content += '--- question\n'
    new_content += english_word
    new_content += '--- answer\n'

    if n % 50 == 0 and n != 0:
        with open(f'spanish_1000/spanish_to_english_1000_{part_n}.ask', 'w') as f:
            f.write(new_content)
            f.close()

        part_n += 1
        new_content = ''

part_n = 1
new_content = ''
for n, line in enumerate(lines):
    line = line.replace(' ', '')
    line_content = line.split('\t')

    spanish_word = line_content[1]
    english_word = line_content[2]

    new_content += english_word  + '\n'
    new_content += '--- question\n'
    new_content += spanish_word
    new_content += '--- answer\n'

    if n % 50 == 0 and n != 0:
        with open(f'spanish_1000/english_to_spanish_1000_{part_n}.ask', 'w') as f:
            f.write(new_content)
            f.close()

        part_n += 1
        new_content = ''
