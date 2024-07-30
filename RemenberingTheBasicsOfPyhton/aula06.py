import random

# random.seed(11)

# random

list_random = [random.randint(1, 1000) for _ in range(10)]
# # print(list_random)

# for n in list_random:
#     if n > 999:
#         break

#     print(n)

# randrange


list_randrange = [random.randrange(10, 17) for _ in range(3)]
random.shuffle(list_randrange)
# print(list_randrange)

random.shuffle(list_randrange)
# # print(list_randrange)

random.shuffle(list_randrange)
# print(list_randrange)


# choice

my_best_friend = random.choice(["Alice", "Bob", "Charlie"]) # "Bob" for me
print(my_best_friend)

# sample

numbers = range(60)
six = random.sample(numbers, 6)
print(six)

