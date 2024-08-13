from math import sqrt, erf

def normal_cdf(x, mu=0,sigma=1):
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2


def normal_approximation_to_binomial(n, p):
    """encontra mi e sigma correspondendo ao Binomial(n, p)"""
    mu = p * n
    sigma = sqrt(p * (1 - p) * n)
    return mu, sigma



# o cdf normal é a probabilidade que a variável esteja abaixo de um limite
normal_probability_below = normal_cdf

# está acima do limite se não estiver abaixo
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# está entre se for menos do que hi, mas não menor do que lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# está fora se não estiver entre
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)
