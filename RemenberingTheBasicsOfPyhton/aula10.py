def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

def f2(x, y):
    return x + y

# g = doubler(f1)
# print(g(3))

g = doubler(f2)
# print(g(1, 2))




def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = { "z" : 3 }
print(other_way_magic(*x_y_list, **z_dict)) # 6
print(*x_y_list) 



def doubler_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    
    return g

g = doubler_correct(f2)
print(g(1, 2))