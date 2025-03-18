from queue import PriorityQueue
#MAGIC constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
directions = [UP,RIGHT,DOWN,LEFT]
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
        #if v != start:
        prev[v] = set() #store all previous to recreate all optional paths
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
                prev[target] = set()
                prev[target].add(u)
                dist[target] = alt_dist
                vertices_queue.put((alt_dist,target))
            elif alt_dist == dist[target]: #to get all best paths store, equivalently good options
                prev[target].add(u)

    return dist, prev



def create_vertices(data):
    start = None
    end = None
    vertices = set()
    height = len(data)
    width = len(data[0])
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
    return vertices, start, end

def create_edges(vertices,start):
    edges = {}
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

    return edges




f = open('data/day16.txt')
data = (f.read()).split()

#create graph and find all distances
vertices, start, end = create_vertices(data)
edges = create_edges(vertices,start)
graph = Graph(vertices,edges)
distances, prev = search(graph,start)
best_end = None 
#Find minimal endnode rotation
for d in distances.keys():
    if d[0] == 1 and d[1]==end[1]:
        if not best_end:
            best_end = d
        elif distances[d] < distances[best_end]:
            best_end = d
        
print('Best end node is:',best_end,'with distance:',distances[best_end])

#recreate all minimal paths
nodes = set()
nodes_to_add = set()
nodes_to_add.add(best_end)

while nodes_to_add:
    new_nodes = set() 
    for node in nodes_to_add:
        nodes.add((node[0],node[1]))
        new_nodes.update(prev[node])

    nodes_to_add = new_nodes

print('Nodes included in some best path:',len(nodes))


