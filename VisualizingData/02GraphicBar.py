from matplotlib import pyplot as plt
from collections import Counter



# movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10]

# xs = [i + 0.1 for i, _ in enumerate(movies)]


# plt.bar(xs, num_oscars, color='black')

# plt.ylabel('# de Premiações')
# plt.title('My favorite movie')

# plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

# plt.show()


 # - - - - - - - - - - - / ////////// / - - - - - - - - - - -

# grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
# decile = lambda grade: grade // 10 * 10

# histogram = Counter(decile(grade) for grade in grades)
# for i, j in histogram.items():
#     print(i, j)


# plt.bar([x for x in histogram.keys()], # move cada barra para a esquerda em 4
#         histogram.values(),  # type: ignore              # dá para cada barra sua altura correta
#         8)                                 # dá para cada barra a largura de 8

# plt.axis((-5, 105, 0, 5))

# plt.xticks([i * 10 for i in range(11)])
# plt.xlabel('Decil')
# plt.ylabel('Qtd. Alunos')
# plt.title('Grades of students')



# plt.show()



 # - - - - - - - - - - - / ////////// / - - - - - - - - - - -


mentions = [500, 505]
years = [2013, 2014]

plt.bar([2013, 2014], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# de vezes que ouvimos alguém dizer 'data science'")

# se você não fizer isso, matplotlib nomeará o eixo x de 0, 1
# e então adiciona a +2.013e3 para fora do canto (matplotlib feio!)
plt.ticklabel_format(useOffset=False)

plt.axis((2012.5, 2014.5, 0, 550))
plt.title('"Olhe o "Grande" Aumento!"')


plt.show()


