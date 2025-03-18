

#x is row and y column for now
#find each group and its perimeter
def bfs(index_x,index_y,data):
    rows = len(data)
    columns = len(data[0])
    visited = set()
    char = data[index_x][index_y]
    perimeter = []
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
                perimeter.append((x-1,y))
            if x < (rows-1) and data[x+1][y] == char: 
                new_nodes.add((x+1,y))
            else:
                perimeter.append((x+1,y))
            if y>0 and data[x][y-1]==char:
                new_nodes.add((x,y-1))
            else:
                perimeter.append((x,y-1))
            if y < (columns-1) and data[x][y+1]==char:
                new_nodes.add((x,y+1))
            else:
                perimeter.append((x,y+1))
        
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
                count += len(new_visited)*len(perimeter)
    return count

def find_fence_cost2(data):
    visited = set()
    rows = len(data)
    columns = len(data[0])
    count = 0
    #find all regions and count the fence price area*(# of edges)
    for i in range(rows):
        for j in range(columns):
            if not((i,j) in visited):
                new_visited, perimeter = bfs(i,j,data)
                visited.update(new_visited)
                edges = count_edges(new_visited,perimeter)
                count += len(new_visited)*edges
    return count



def count_edges(group,perimeter):
    side_count = 0
    already_counted = set()
    for node in group:
        if not (node in already_counted):
            x = node[0]
            y = node[1]
            if ((x+1,y) in perimeter):
                while ((x,y) in group) and ((x+1,y) in perimeter):
                    already_counted.add((x,y))
                    y += 1
                x = node[0]
                y = node[1]
                while ((x,y) in group) and ((x+1,y) in perimeter):
                    already_counted.add((x,y))
                    y -= 1
                side_count += 1
    
    already_counted = set()
    for node in group:
        if not (node in already_counted):
            x = node[0]
            y = node[1]
            if ((x-1,y) in perimeter):
                while ((x,y) in group) and ((x-1,y) in perimeter):
                    already_counted.add((x,y))
                    y += 1
                x = node[0]
                y = node[1]
                while ((x,y) in group) and ((x-1,y) in perimeter):
                    already_counted.add((x,y))
                    y -= 1
                side_count += 1
    already_counted = set()
    for node in group:
        if not (node in already_counted):
            x = node[0]
            y = node[1]
            if ((x,y+1) in perimeter):
                while ((x,y) in group) and ((x,y+1) in perimeter):
                    already_counted.add((x,y))
                    x += 1
                x = node[0]
                y = node[1]
                while ((x,y) in group) and ((x,y+1) in perimeter):
                    already_counted.add((x,y))
                    x -= 1
                side_count += 1

    already_counted = set()
    for node in group:
        if not (node in already_counted):
            x = node[0]
            y = node[1]
            if ((x,y-1) in perimeter):
                while ((x,y) in group) and ((x,y-1) in perimeter):
                    already_counted.add((x,y))
                    x += 1
                x = node[0]
                y = node[1]
                while ((x,y) in group) and ((x,y-1) in perimeter):
                    already_counted.add((x,y))
                    x -= 1
                side_count += 1

    return side_count

        



f = open('data/day12.txt')
data = (f.read()).split()
print('The cost of the fence is:',find_fence_cost(data))
print('The cost of the fence after discount is:',find_fence_cost2(data))