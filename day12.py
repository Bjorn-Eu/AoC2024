

#x is row and y column for now
def bfs(index_x,index_y,data):
    rows = len(data)
    columns = len(data[0])
    visited = set()
    char = data[index_x][index_y]
    perimeter = 0
    nodes_to_explore = set()
    nodes_to_explore.add((index_x, index_y))
    visited.update(nodes_to_explore)

    while nodes_to_explore:
        new_nodes = set()
        for node in nodes_to_explore:
            x = node[0]
            y = node[1]
            #move left
            if x > 0 and data[x-1][y] == char:
                new_nodes.add((x-1,y))
            else:
                perimeter += 1
            if x < (rows-1) and data[x+1][y] == char: 
                new_nodes.add((x+1,y))
            else:
                perimeter += 1
            if y>0 and data[x][y-1]==char:
                new_nodes.add((x,y-1))
            else:
                perimeter += 1
            if y < (columns-1) and data[x][y+1]==char:
                new_nodes.add((x,y+1))
            else:
                perimeter += 1
        
        nodes_to_explore = new_nodes.difference(visited) #don't revisit
        visited.update(new_nodes)
    return visited, perimeter


def find_fence_cost(data):
    visited = set()
    rows = len(data)
    columns = len(data[0])
    count = 0
    #find all regions and count the fence price (area*perimeter)
    for i in range(rows):
        for j in range(columns):
            if not((i,j) in visited):
                new_visited, perimeter = bfs(i,j,data)
                visited.update(new_visited)
                count += len(new_visited)*perimeter
    return count






f = open('data/day12.txt')
data = (f.read()).split()
print(find_fence_cost(data))