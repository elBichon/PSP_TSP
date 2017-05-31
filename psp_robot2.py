import random

size = 10
nb_zero = 0
nb_one = 0
square_size = (size*size)/2
indicator = random.randint(0,1)

def createMat(square_size, nb_zero, nb_one)
    if nb_zero != square_size && nb_one != square_size:
        [[random.randint(0,1) for i in range(column)] for j in range(line)]
createMat(size, size)


for line in createMat(size, size):
    print(line)