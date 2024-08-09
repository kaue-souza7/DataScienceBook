# import random

# def random_kid():
#     return random.choice(['boy', 'girl'])

# both_girls = 0
# older_girl = 0
# either_girl = 0

# random.seed(0)

# for _ in range(10000):
#     younger = random_kid()
#     older = random_kid()

#     if older == 'girl':
#         older_girl += 1
#     if older == 'girl' and younger == 'girl':
#         both_girls += 1
#     if older == 'girl' or younger == 'girl':
#         either_girl += 1

# # "|" <--- condicionado por: ---> "|"
# print(f'P(both | older): {both_girls / older_girl}')
# print(f'P(both | either): {both_girls / either_girl}')


PTD = 0.99
PD = 0.0001
PTND = 0.01
PND = 0.9999


print(f'A P(D|T): {(PTD * PD / PTD *PD + PTND * PND) * 100}')