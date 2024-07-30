from matplotlib import pyplot as plt



variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]


# podemos fazer múltiplas chamadas para plt.plot
# para mostrar múltiplas séries no mesmo gráfico
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs, total_error, 'b:', label='total error')


# porque atribuímos rótulos para cada série
# podemos obter uma legenda gratuita
# loc=9 significa “top center”
plt.legend(loc=9)
plt.xlabel('Complexidade do modelo')
plt.title("Compromisso entre Polarização e Variância")


plt.show()
