
def teleport_options(path,index):
    shortcuts = []
    x = index[1]
    y = index[0]
    position = path.index(index)
    if (y+2,x) in path:
        shortcuts.append(path.index((y+2,x))-position-2)
    if (y-2,x) in path:
        shortcuts.append(path.index((y-2,x))-position-2)
    if (y,x+2) in path:
        shortcuts.append(path.index((y,x+2))-position-2)
    if (y,x-2) in path:
        shortcuts.append(path.index((y,x-2))-position-2)
    if (y+1,x+1) in path:
        shortcuts.append(path.index((y+1,x+1))-position-2)
    if (y-1,x-1) in path:
        shortcuts.append(path.index((y-1,x-1))-position-2)
    return shortcuts

def search_path(array,start,end):
    node = start
    visited = []
    steps = 0
    while node != end:
        visited.append(node)
        x = node[1]
        y = node[0]
        if array[y+1][x] == '.':
            if not (y+1,x) in visited:
                node = (y+1,x)
        if array[y-1][x] == '.':
            if not (y-1,x) in visited:
                node = (y-1,x)
        if array[y][x+1] == '.':
            if not (y,x+1) in visited:
                node = (y,x+1)
        if array[y][x-1] == '.':
            if not (y,x-1) in visited:
                node = (y,x-1)
        steps += 1
    visited.append(end)
    return visited

f = open('data/day20.txt')
data = (f.read()).split()
height = len(data)
width = len(data[0])
array = []
for d in data:
    array.append([x for x in d])

start = None
end = None
for i in range(height):
    for j in range(width):
        if array[i][j] == 'S':
            start = (i,j)
            array[i][j] = '.'
        elif array[i][j] == 'E':
            end = (i,j)
            array[i][j] = '.'

print(start)
print(end)
path = search_path(array,start,end)
print(len(path))


print(teleport_options(path,end))
total_shortcuts = []
for position in path:
    shortcuts = teleport_options(path,position)
    for s in shortcuts:
        total_shortcuts.append(s)

table = {}
for p in total_shortcuts:
    if p in table.keys():
        table[p] += 1
    else:
        table[p] = 1
count = 0

for key in sorted(table.keys()):
    if key > 0:
        print('There are ',table[key],' shortcuts saving ',key,' picoseconds')
    if key >= 100:
        count += table[key]

print('Number of cheats that save at least 100 picoseconds are', count)

table = []
for i in range(len(path)):
    p = path[i]
    for j in range(i,len(path)):
        p2 = path[j]
        val = abs(p2[0]-p[0])+abs(p2[1]-p[1]) #manhattan distance
        if val>0 and val<=20:
            table.append(j-i-val)

print('Number of cheats: ',len(table))

#part II

new_table = {}
for k in table:
    if k in new_table.keys():
        new_table[k] += 1
    else:
        new_table[k] = 1

count = 0
for key in sorted(new_table.keys()):
    if key >= 50:
        print('There are ',new_table[key],' shortcuts saving ',key,' picoseconds')
    if key >= 100:
        count += new_table[key]
print(new_table)


print('Number of cheats that save at least 100 picoseconds are', count)
