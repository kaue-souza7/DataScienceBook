from statistics import variance, correlation, covariance, mean
list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
          55, 60, 65, 70, 75, 80, 85, 90, 95, 100,
          105, 110, 115, 120, 125, 130, 135, 140, 145, 150,
          155, 160, 165, 170, 175, 180, 185, 190, 195, 200,
          205, 210, 215, 220, 225, 230, 235, 240, 245, 250]


list2 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
          60, 65, 70, 75, 80, 85, 90, 95, 100, 105,
          110, 115, 120, 125, 130, 135, 140, 145, 150, 155,
          160, 165, 170, 175, 180, 185, 190, 195, 200, 205,
          210, 215, 220, 225, 230, 235, 240, 245, 250, 255]


# Variance list1 and mean
print(mean(list1))
print(f'VARIANCE LIST1: {variance(list1)}')


# Variance list2 and mean
print(mean(list2))
print(f'VARIANCE LIST2: {variance(list2)}')


# Covariance das list
print(f'COVARIANCE: {covariance(list1, list2)}') # Esperado: Positiva


# Correlation das list
print(f'CORRELATION: {correlation(list1, list2)}') # Esperado: Proximo de 1

from matplotlib import pyplot as plt

plt.scatter(list1, list2, color='blue', marker='o')
plt.show()
