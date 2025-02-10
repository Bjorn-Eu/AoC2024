
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


def entropi(lin_data):
    lensig=lin_data.size
    symset=list(set(lin_data))
    numsym=len(symset)
    propab=[np.size(lin_data[lin_data==i])/(1.0*lensig) for i in symset]
    ent=np.sum([p*np.log2(1.0/p) for p in propab])
    return ent

f = open('data/day14.txt')
data = f.read()

data = list(map(float,re.findall("[-]?\\d+",data)))

length = len(data)
steps = 100
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

positions = {}
for i in range(length//4):
    pos = find_pos(px[i],py[i],vx[i],vy[i],steps)
    if pos in positions.keys():
        positions[pos] += 1
    else:
        positions[pos] = 1


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



graph = np.zeros((10500))
for j in range(10500):
    print("Printing iteration: ",j)
    taken = set()
    grid = np.zeros((X_RANGE,Y_RANGE))
    
    for i in range(length//4):
        pos = find_pos(px[i],py[i],vx[i],vy[i],j)
        grid[pos[0]][pos[1]]  = 1.0
        taken.add(pos)

    #print(grid)
    grid_l = grid.reshape(-1)
    #print(sum(grid_l))
    ent = entropi(grid_l)
    #print(entropi(grid_l))
    graph[j] = ent


plt.plot(np.array(range(10500)),graph)
plt.show()
print(np.argmax(graph))


grid = np.zeros((X_RANGE,Y_RANGE))
for i in range(length//4):
    pos = find_pos(px[i],py[i],vx[i],vy[i],7709)
    grid[pos[0]][pos[1]]  = 1.0
grid[pos[0]][pos[1]]  = 1.0
for i in range(Y_RANGE):
    for j in range(X_RANGE):
        if grid[j][i] == 1:
            print("*",end="")
        else:
            print("_",end="")
    print("")