





even_numbers = [
    x
    for x in range(50)
    if x % 2 == 0
]

for x in even_numbers:
    ...
    # print(x)


square_numbers: dict = {
    x: x*x
    for x in range(10)

}

# print(square_numbers)

# for x, qx in square_numbers.items():
#     print(x, qx)

print()
print()
print()
print()
print()
print()

only_squares = [
    (x, y)
    for x in range(10)
    for y in range(10)
]
   

print(only_squares)
