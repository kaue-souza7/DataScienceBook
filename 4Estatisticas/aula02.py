
from aula01 import *
from statistics import mean, median, variance, covariance, correlation

print(mean(num_friends))

# Algumas vezes também nos interessaremos pela mediana, que é o valor maior
# do meio (se o número de pontos de dados for ímpar) ou a média dos dois valores
# que estiverem bem no meio (se o número de pontos de dados for par).


print(median(num_friends))

def sum_of_squares(v):
    """computa a soma dos elementos ao quadrado em v"""
    return sum(v_i ** 2 for v_i in v)


def data_range(x):
    return max(x) - min(x)

print(data_range(num_friends))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
    for v_i, w_i in zip(v, w))

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

import math

def standard_deviation(x):
    return math.sqrt(variance(x))



def variance_(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)

daily_minutes = [
    30, 45, 60, 15, 40, 55, 20, 35, 50, 25, 60, 5, 30, 45, 60, 15, 40, 55, 20, 35,
    50, 25, 60, 5, 30, 45, 60, 15, 40, 55, 20, 35, 50, 25, 60, 5, 30, 45, 60, 15,
    40, 55, 20, 35, 50, 25, 60, 5, 30, 45, 60, 15, 40, 55, 20, 35, 50, 25, 60, 5,
    30, 45, 60, 15, 40, 55, 20, 35, 50, 25, 60, 5, 30, 45, 60, 15, 40, 55, 20, 35,
    50, 25, 60, 5, 30, 45, 60, 15, 40, 55, 20, 35, 50, 25, 60, 5, 30, 45, 60, 15,
    40, 55, 20, 35, 50, 25, 60, 5, 30, 45, 60, 15, 40, 55, 20, 35, 50, 25, 60, 5,
    30, 45, 60, 15, 40, 55, 20, 35, 50, 25, 60, 5, 30, 45, 60, 15, 40, 55, 20, 35,
    50, 25, 60, 5, 30, 45, 60, 15, 40, 55, 20, 35, 50, 25, 60, 5, 30, 45, 60, 15
]


def covariance_(x: list[int], y: list[int]):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

print(covariance_(num_friends, daily_minutes))
print(covariance(num_friends, daily_minutes))


def correlation_(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    print(stdev_x)
    print(stdev_y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # se não houver amplitude, a correlação é zero
print(correlation_(num_friends, daily_minutes)) # -0.094
print(correlation(num_friends, daily_minutes)) # -0.094



outlier = num_friends.index(50) 

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]
daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]
print(correlation(num_friends_good, daily_minutes_good) ) # - 0.1



# ------------------   DEFINIÇÃO DE COVARIÂNCIA
# Sim, é normal a covariância ser negativa. A covariância é uma medida da direção 
# conjunta de duas variáveis. Se a covariância for positiva, isso indica que, em 
# média, as duas variáveis aumentam juntas (ou diminuem juntas). Se a covariância 
# for negativa, isso indica que, em média, uma variável aumenta enquanto a outra 
# diminui.





# print()

# print(variance_(num_friends))
# print(variance(num_friends))