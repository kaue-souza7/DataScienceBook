


filename = 'file'

# 'r' significa somente leitura
file_for_reading = open('reading_file.txt', 'r')

# 'w' é escrever - - destruirá o arquivo se ele já existir!
file_for_writing = open('writing_file.txt', 'w')

# 'a' é anexar - - para adicionar ao final do arquivo
file_for_appending = open('appending_file.txt', 'a')

# não se esqueça de fechar os arquivos ao terminar
file_for_writing.close()

with open(filename, 'r', encoding='utf8') as file:
    # data = function
    ...




