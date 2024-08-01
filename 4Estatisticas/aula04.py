from statistics import correlation

x = [-2, -1, 0, 1, 2]
y = [ 2,  1, 0, 1, 2]


print(correlation(x, y))

a = [-2, 1, 0, 1, 2]
b = [99.98, 99.99, 100, 100.01, 100.02]

print(round(correlation(a, b), 2))
