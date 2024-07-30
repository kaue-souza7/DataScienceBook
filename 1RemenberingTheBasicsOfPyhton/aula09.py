# COMPACTANDO

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4]

new_list = list(zip(list1, list2))
print(new_list)

# DESCOMPACTANDO

letters, numbers = map(list, zip(*new_list)) 
# O asterisco desempenha a descompactação de argumento
print(numbers)
print(letters)