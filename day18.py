#magic constants
GRID_SIZE = 71

def bfs(grid):
    visited = set()
    to_visit = set()
    start = (0,0)
    to_visit.add(start)
    end = (GRID_SIZE-1,GRID_SIZE-1)
    steps = 0
    while to_visit:
        new_nodes = set()
        for node in to_visit:
            y = node[0]
            x = node[1]
            if (x>0) and grid[y][x-1] == 0:
                new_nodes.add((y,x-1))
            if (x<(GRID_SIZE-1)) and grid[y][x+1]==0:
                new_nodes.add((y,x+1))
            if (y>0) and grid[y-1][x] == 0:
                new_nodes.add((y-1,x))
            if (y<(GRID_SIZE-1)) and grid[y+1][x] == 0:
                new_nodes.add((y+1,x))
        visited.update(to_visit)
        to_visit = new_nodes.difference(visited)
        if end in visited:
            print('Found end')
            break
        steps += 1

    return steps

            



f = open('data/day18.txt')
data = f.read().split()
positions = [list(map(int,data[i].split(','))) for i in range(len(data))]




grid = [[0]*GRID_SIZE for i in range(GRID_SIZE)]

iterations = 3042 #1024 part I
print(positions)

for i in range(iterations):
    x = (positions[i])[0]
    y = (positions[i])[1]
    grid[y][x] = 1

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] == 1:
            print('#',end='')
        else:
            print('.',end='')
    print('')

steps = bfs(grid)
print(steps)

print(positions[3042])