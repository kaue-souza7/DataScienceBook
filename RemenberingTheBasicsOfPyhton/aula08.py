def exp(base, power):
    return base ** power

# def two_to_the(power):
#     return exp(2, power)

# ORRRR


from functools import partial, reduce

two_to_the = partial(exp, 2)
print(two_to_the(2))

# ARGUMENTS NAMED

square_of = partial(exp, power=2)
print(square_of(4))

print()
print()
print()

def double(x):
    return x * 2

def str_(*args):
    for arg in args:
        return str(arg)

numbers = [1, 2, 3, 4]

twice_numbers = [double(n) for n in numbers] # [2, 4, 6, 8]
print(twice_numbers)
print(type(twice_numbers[0]))


twice_numbers = map(str, numbers) # igual ao de cima
print([*twice_numbers])
print(type(twice_numbers))

list_doubler = partial(map, double) # função que duplica a lista
twice_numbers = list_doubler(numbers)
print(list(twice_numbers))

print()
print()
print()
print()
print()
print()

def multiply(x, y): 
    return x * y


products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]
print(list(products))


def is_even(n):
    """True se x for par, False se x for ímpar"""
    return n % 2 == 0


numbers_even = [n for n in numbers if is_even(n)] # [2, 4]
print(numbers_even)



numbers_even = filter(is_even, numbers) # igual ao de cima
print(list(numbers_even))


list_evener = partial(filter, is_even) # função que filtra a lista
numbers_even = list_evener(numbers) # novamente [2, 4]
print(list(numbers_even)) 


print()
print()
print()
print()
print()
print()
print()

n_product = reduce(multiply, numbers) # = 1 * 2 * 3 * 4 = 24
print(n_product)
n_product = 0

list_product = partial(reduce, multiply) # função que reduz uma lista
n_product = list_product(numbers) # novamente = 24
print(n_product)


