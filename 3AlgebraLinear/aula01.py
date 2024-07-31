import math



height_weight_age = [70, # polegadas,
                    170, # quilos,
                    40 ] # anos


grades = [95, # teste1
        80, # teste2
        75, # teste3
        62 ] # teste4




def vector_subtract(v, w):
    return [vi - wi for vi, wi in zip(v, w)]


def magnitude(vector):
    return math.sqrt(sum(x**2 for x in vector))


def distance(v, w):
    return magnitude(vector_subtract(v, w))


v = [3, 4]
w = [0, 0]

dist = distance(v, w)
print(dist)  # Saída: 5.0


# Subtração Vetorial: v - w = [3-0, 4-0] = [3, 4]
# Magnitude do Vetor: 
# magnitude([3, 4]) = sqtr(3²+4²) = sqtr(9+16) = sqtr(25) = 5