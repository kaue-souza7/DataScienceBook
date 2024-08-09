import scipy.stats as stats


# Parâmetros da distribuição normal
mu = 0 # média
sigma = 1 # desvio padrão

# Calcular a CDF para um valor especifico
x = 1.5
cdf_value = stats.norm.cdf(x, mu, sigma)

print(f"O valor da CDF para x={x} é {cdf_value}")