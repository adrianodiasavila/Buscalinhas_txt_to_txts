import os

def merge_unique_lines(directory, output_file):

    lines_seen = set()

    with open(output_file, 'w',  encoding='utf-8') as outfile:

        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as infile:
                    for line in infile:
                        if line not in lines_seen:
                            outfile.write(line)
                            lines_seen.add(line)


merge_unique_lines(r'C:\Users\Adriano\Desktop\STRINGS DE BUSCA\PESQUISAS FEITAS\SET', 'set.txt')