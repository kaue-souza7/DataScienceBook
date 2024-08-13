



import csv
from pathlib import Path

FILE_NAME = Path().parent.resolve() / '7ObtencaoDeDados' / 'acoes.csv'
date_list = []
symbol_list = []
price_list = []

with open(FILE_NAME, 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        date_list.append(row[0].split()[0])
        symbol_list.append(row[0].split()[1])
        price_list.append(row[0].split()[2])

# print(date_list)


from matplotlib import pyplot as plt

plt.bar(symbol_list, price_list, 0.8)



plt.show()