
def search_trails(grid):
    rows =len(grid)
    columns = len(grid[0])
    count = 0 
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 0:
                count += len(step(i,j,grid))
    return count

def step(x,y,grid):
    rows =len(grid)
    columns = len(grid[0])
    reachable = set()

    height = grid[x][y]
    if height == 9:
        reachable.add((x,y))
        return reachable
    if x<rows-1:
        if grid[x+1][y] == (height+1):
            reachable.update(step(x+1,y,grid))

    if x>0:
        if grid[x-1][y]== height+1:
            reachable.update(step(x-1,y,grid))

    if y>0:
        if grid[x][y-1] == height+1:
            reachable.update(step(x,y-1,grid))
    if y<columns-1:
        if grid[x][y+1] == height+1:
            reachable.update(step(x,y+1,grid))
    return reachable


def search_trails2(grid):
    rows =len(grid)
    columns = len(grid[0])
    count = 0 
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 0:
                count += step2(i,j,grid)
    return count

def step2(x,y,grid):
    rows =len(grid)
    columns = len(grid[0])
    count = 0

    height = grid[x][y]
    if height == 9:
        return 1
    if x<rows-1:
        if grid[x+1][y] == (height+1):
            count += step2(x+1,y,grid)

    if x>0:
        if grid[x-1][y]== height+1:
            count += step2(x-1,y,grid)

    if y>0:
        if grid[x][y-1] == height+1:
            count += step2(x,y-1,grid)
    if y<columns-1:
        if grid[x][y+1] == height+1:
            count += step2(x,y+1,grid)
    return count


f = open('data/day10.txt','r')
data = f.read().split()
columns = len(data[0])
rows = len(data)
grid = [[0]*columns]*rows
for i in range(rows):
        grid[i] = list(map(int,data[i]))




print('Number of hiking trails:',search_trails(grid))
print('Hiking trail rating sum:', search_trails2(grid))
