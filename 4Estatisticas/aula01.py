
from matplotlib import pyplot as plt
from collections import Counter



num_friends = [
    10, 23, 45, 12, 22, 33, 47, 5, 30, 21, 50, 0, 14, 28, 38, 19, 43, 27, 16, 41,
    8, 39, 46, 24, 18, 31, 7, 29, 15, 42, 20, 48, 26, 49, 3, 40, 13, 25, 4, 34,
    6, 44, 17, 50, 9, 32, 11, 37, 35, 22, 43, 12, 28, 16, 30, 45, 19, 50, 29, 23,
    14, 40, 33, 26, 9, 41, 20, 38, 31, 25, 47, 18, 12, 46, 22, 35, 4, 0, 48, 27,
    50, 39, 8, 21, 6, 44, 30, 13, 42, 24, 19, 47, 32, 10, 33, 45, 11, 28, 7, 38,
    22, 50, 15, 20, 43, 26, 14, 37, 9, 48, 31, 18, 12, 46, 27, 49, 21, 34, 6, 45,
    0, 19, 29, 39, 33, 24, 38, 11, 43, 30, 5, 22, 50, 12, 26, 40, 32, 15, 48, 21,
    44, 1, 1, 1, 10, 28, 37, 6, 42, 9, 50, 13, 45, 19, 31, 29, 47, 8, 30, 24, 41, 33, 18
]

for x in num_friends:
    if x == 0:
        num_friends.remove(x)


friend_counts = Counter(num_friends)
# print(friend_counts)

xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys, 1.5)
plt.axis((0, 101, 0, 25))

plt.title("Histograma da Contagem de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("# de pessoas")


# plt.show()

num_points = len(num_friends)
# print(num_points)
largest_value = max(num_friends)
smallest_value = min(num_friends)
print(smallest_value)
print(largest_value)


sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]  # 1
second_smallest_value = sorted_values[1] # 1
second_largest_value = sorted_values[-2] # 49


