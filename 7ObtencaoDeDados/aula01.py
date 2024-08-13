# egrep.py
import sys, re

# sys.argv é a lista dos argumentos da linha de comandos
# sys.argv [0] é o nome do programa em si
# sys.argv [1] será o regex especificado na linha de comandos

print(f'argv0 is: {sys.argv[0]}')


regex = sys.argv[1]
# regex = 'pass'
# para cada linha passada pelo script
for line in sys.stdin:
    # se combinar com o regex, escreva-o para o stdout
    if re.search(regex, line):
        sys.stdout.write(f'your line is: {line}')
        print('The secrets numbers are:')
        for x in range(11):
            print(f'\t {x}')







