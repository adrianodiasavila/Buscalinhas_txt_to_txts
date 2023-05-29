import os

listfile = str(input('Especifique o arquivo .txt contendo as linhas para buscar: '))
searchfolder = str(input('Especifique a pasta contendo arquivos .txt onde buscar: '))

with open(listfile, 'r', encoding='utf-8') as f:
    titulos = [line.strip() for line in f.readlines()]

results = []

for filename in os.listdir(searchfolder):

    with open(f'{searchfolder}\\{filename}', 'r', encoding='utf-8') as file:
        file_content = file.read().lower()

        file_results = []

        for line in titulos:
            search_text = line.split(';')[1].strip().lower()

            if search_text in file_content:
                file_results.append(line)

        results.append(filename)
        if file_results:
            results.extend(file_results)
        else:
            results.append("Nada encontrado")

        results.append('')

with open('Results.txt', 'w') as f:
    f.write('\n'.join(results))