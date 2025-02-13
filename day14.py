
import re
import numpy as np
import matplotlib.pyplot as plt
#magic contants
X_RANGE = 101
Y_RANGE = 103

#finds the position after n iterations
def find_pos(px,py,vx,vy,n):
    xpos = (int)((px+vx*n)%X_RANGE)
    ypos = (int)((py+vy*n)%Y_RANGE)
    return (xpos,ypos)



f = open('data/day14.txt')
data = f.read()
data = list(map(float,re.findall("[-]?\\d+",data)))
length = len(data)
steps = 100
#prepare data
px = []
py = []
vx = []
vy = []
for i in range(length):
    if i%4==0:
        px.append(data[i])
    elif i%4==1:
        py.append(data[i])
    elif i%4==2:
        vx.append(data[i])
    else:
        vy.append(data[i])

#find positions efter steps iterations
positions = {}
for i in range(length//4):
    pos = find_pos(px[i],py[i],vx[i],vy[i],steps)
    if pos in positions.keys():
        positions[pos] += 1
    else:
        positions[pos] = 1

#count sum in each quarter
countQ1=0
countQ2=0
countQ3=0
countQ4=0
for pos in positions.keys():
    if pos[0] < X_RANGE//2:
        if pos[1]< Y_RANGE//2:
            countQ1 += positions[pos]
        elif pos[1]>Y_RANGE//2:
            countQ2 += positions[pos]
    elif pos[0]>X_RANGE//2:
        if pos[1]< Y_RANGE//2:
            countQ3 += positions[pos]
        elif pos[1]>Y_RANGE//2:
            countQ4 += positions[pos]


print("The count is",countQ1*countQ2*countQ3*countQ4)


#calculate entropi for each configuration
#conjecture that a picture should have high entropi
graph = np.zeros((10500))
for j in range(10500):
    if j%1000==0: #give some update to user.
        print("Iteration: ",j)
    taken = set()
    grid = np.zeros((X_RANGE,Y_RANGE))
    
    for i in range(length//4):
        pos = find_pos(px[i],py[i],vx[i],vy[i],j)
        grid[pos[0]][pos[1]]  = 1.0
        taken.add(pos)
    #number of unique nodes
    graph[j] = sum(sum(grid))


#finding the index where least number overlap seems to work
#node one get similar by taking the binary Shannon entropi
tree_index = np.argmax(graph)

#print our found Christmas tree (config with most nodes)
grid = np.zeros((X_RANGE,Y_RANGE))
for i in range(length//4):
    pos = find_pos(px[i],py[i],vx[i],vy[i],tree_index)
    grid[pos[0]][pos[1]]  = 1.0
grid[pos[0]][pos[1]]  = 1.0
for i in range(Y_RANGE):
    for j in range(X_RANGE):
        if grid[j][i] == 1:
            print("*",end="")
        else:
            print("_",end="")
    print("")