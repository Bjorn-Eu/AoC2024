

def step(x,y,direction,grid):
    if direction == 'up':
        if array[y-1][x] == EMPTY:
            y -= 1
        else: #found wall
            direction = 'right'
    elif direction == 'right':
        if array[y][x+1] == EMPTY:
            x += 1
        else: #found wall
            direction = 'down'

    elif direction == 'down':       
        if array[y+1][x] == EMPTY:
            y += 1
        else: #found wall
            direction = 'left'
    else:
        if array[y][x-1] == EMPTY:
            x -= 1
        else: #found wall
            direction = 'up'
    return x,y,direction

def find_path(x,y,grid):
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    visited.add((x,y))
    direction = 'up'
    inside = True
    while inside:
        x,y,direction = step(x,y,direction,grid)
        visited.add((x,y))
        left = (x==0 and direction == 'left')
        right = (x==(columns-1) and direcition =='right')
        up = (y == 0 and (rows-1) and direction =='up')
        down = (y==(rows-1) and direction =='down')
        if left or right or up or down:
            break
    return visited

def is_loop(x,y,grid):
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    
    direction = 'up'
    visited.add((x,y,direction))
    inside = True
    while inside:
        x,y,direction = step(x,y,direction,grid)
        if (x,y,direction) in visited:
            return True
        visited.add((x,y,direction))
        left = (x==0 and direction == 'left')
        right = (x==(columns-1) and direction =='right')
        up = (y == 0 and (rows-1) and direction =='up')
        down = (y==(rows-1) and direction =='down')
        if left or right or up or down:
            return False


def find_loops(candidates,x,y,grid):
    obstacles = set()
    for c in candidates:
        grid[c[1]][c[0]] = 'O' #add obstacle
        if is_loop(x,y,grid):
            obstacles.add(c)
        grid[c[1]][c[0]] = '.'

    return obstacles

    



f = open('data/day6.txt','r')
data = f.read().split('\n')
array = []

for d in data:
    array.append(list(d))

start_index = None
rows = len(array)
columns = len(array[0])
directions = ['up','right','down','left']

direction = 'up'
EMPTY = '.'


#find start index and remove marker
for i in range(rows):
    for j in range(columns):
        if array[i][j] == '^':
            start_index = (i,j)
            array[i][j] = EMPTY #so we can pass start position



visited = set(start_index)
x = start_index[1]
y = start_index[0]

visited = find_path(x,y,array)
print('Number of visited positions:',len(visited))



visited.remove((x,y))
obstacles = find_loops(visited,x,y,array)
print('Number of posible obstacle positions:',len(obstacles))





