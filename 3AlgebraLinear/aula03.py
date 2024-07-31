friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]



friendships_matriz = [[0
                        for j in range(10)]
                        for i in range(10)]


# ISSO 
# for i, r in enumerate(friendships_matriz):
#     for x, y in friendships:
#         if i == x:
#             r[y] = 1
#         elif i == y:
#             r[x] = 1

# OU ISSO - mais recomendado e mais prático
for x, y in friendships:
    friendships_matriz[x][y] = 1
    friendships_matriz[y][x] = 1



for i in friendships_matriz:
    print(i)