import random
import math
dimension = 100


dist_of_gradients = 10

gradients_num = int((dimension*dimension)/dist_of_gradients)

grid = [[dimension]]
#Begin with 2-dimensional perlin noise
#To make a perlin noise it's necessary to build at first a grid
gradients = [[]]
#Let's insert into the grid all gradient with random strength (between -1 and 1) and a random orientation
# a gradient has an x and a y that are defined with the sin and cosin func
for i,j in range(gradients_num):
    theta = random.uniform(0,2*math.pi)
    module = random.uniform(0,1)
    gradients[i][j]=(math.cos(theta),math.sin(theta))

#I filled the grid with gradients with random orientation(gived by theta) and random module

#Now i will do the dot product for each point in the grid and with each other gradients

for i,j in range(dimension):
    for k,h in gradients:
        pos = (i-(k*dist_of_gradients),j-(h*dist_of_gradients))
        grid[i][j] = pos[0]*(gradients[i][j][0]+(k*dist_of_gradients))+pos[1]*(gradients[i][j][1]+(h*dist_of_gradients))

print(grid)

