from queue import PriorityQueue
#MAGIC constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
INFINITY = 10**10
TURN_COST = 1000
TRAN_COST = 1


class Edge:
    def __init__(self,target,weight):
        self.target = target
        self.weight = weight

class Graph:
    def __init__(self,vertices,edges):
        self.vertices = vertices #expect set
        self.edges = edges #expect dictionary

    def get_neighbours(self,v):
        if v in self.edges.keys():
            return self.edges[v]
        else:
            return set()



#Djikstra's algorithm
def search(graph,start):
    prev = {}
    dist = {}
    vertices_queue = PriorityQueue(1000)
    
    #add the other vertices
    for v in graph.vertices:
        if v != start:
            prev[v] = None
            dist[v] = INFINITY
    
    #add start to queue
    vertices_queue.put((0,start))
    dist[start] = 0
    
    while vertices_queue.qsize()>0:
        val,u = vertices_queue.get() #get minimum distance vertex and remove it
        for n in graph.get_neighbours(u):
            target = n.target
            weight = n.weight
            alt_dist = dist[u] + weight
            if alt_dist < dist[target]:
                prev[target] = u
                dist[target] = alt_dist
                vertices_queue.put((alt_dist,target))
    return dist





f = open('data/day16.txt')
data = (f.read()).split()


directions = [UP,RIGHT,DOWN,LEFT]
end = None
Start = None
height = len(data)
width = len(data[0])

vertices = set()
edges = {}


#create vertices
for i in range(height):
    for j in range(width):
        if data[i][j] != '#':
            #add nodes
            for direction in directions:
                vertices.add((i,j,direction))
            if data[i][j] == 'S':
                start = (i,j,RIGHT)
            elif data[i][j] == 'E':
                end = (i,j,RIGHT)
#create edges
vert2 = set()
vert2.add(start)
for v in vertices:
    y = v[0]
    x = v[1]
    dir = v[2]
    edges[v] = set()
    if dir == UP:
        edges[v].add(Edge((y,x,RIGHT),TURN_COST))
        edges[v].add(Edge((y,x,LEFT),TURN_COST))
        if (y-1,x,UP) in vertices:
            edges[v].add(Edge((y-1,x,UP),TRAN_COST))
    elif dir == RIGHT:
        edges[v].add(Edge((y,x,UP),TURN_COST))
        edges[v].add(Edge((y,x,DOWN),TURN_COST))
        if (y,x+1,RIGHT) in vertices:
            edges[v].add(Edge((y,x+1,RIGHT),TRAN_COST))
    elif dir == DOWN:
        edges[v].add(Edge((y,x,RIGHT),TURN_COST))
        edges[v].add(Edge((y,x,LEFT),TURN_COST))
        if (y+1,x,DOWN) in vertices:
            edges[v].add(Edge((y+1,x,DOWN),TRAN_COST))
    else:
        edges[v].add(Edge((y,x,UP),TURN_COST))
        edges[v].add(Edge((y,x,DOWN),TURN_COST))
        if (y,x-1,LEFT) in vertices:
            edges[v].add(Edge((y,x-1,LEFT),TRAN_COST))


#create graph and find all distances
graph = Graph(vertices,edges)
distances = search(graph,start)

#Print all end states, the minimum is the answer
for d in distances.keys():
    if d[0] == 1 and d[1]==end[1]:#end[0] and d[0] == end[1]:
        print('Node:',d,'With distance',distances[d])

