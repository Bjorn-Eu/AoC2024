import itertools

max_clusters = []
class Graph:
    def __init__(self):
        pass

#Bron-Kerborsch algorithm
def find_complete_subgraphs(R,P,X,edges):
    if (not P) and (not X):
        max_clusters.append(R)
    else:
        oldP = P.copy()
        for v in oldP:
            neighbours = edges[v]
            find_complete_subgraphs(R.union(set([v])),P.intersection(neighbours),X.intersection(neighbours),edges)
            P.remove(v)
            if v in X:
                X.remove(v)

f = open('data/day23.txt')
data = (f.read()).split()
connections = []
for d in data:
    connection = list(d.split('-'))
    connections.append(connection)

t_connections = []
nt_connections = []

edges = {}
for connection in connections:
    first = connection[0]
    second = connection[1]
    if first in edges.keys():
        edges[first].add(second)
    else:
        edges[first] = set()
        edges[first].add(second)
    if second in edges.keys():
        edges[second].add(first)
    else:
        edges[second] = set()
        edges[second].add(first)


T_edges = {}
for edge in edges.keys():
    if edge[0] == 't':
        T_edges[edge] = edges[edge]

for connection in connections:
    added = False
    for c in connection:
        if c[0] == 't':
            t_connections.append(connection)
            added = True
            break
    if not added:
        nt_connections.append(connection)
    
    

#heap seems good?

length = len(t_connections)
values = set()
for t_edge in T_edges.keys():
    target = T_edges[t_edge]
    for t1,t2 in itertools.combinations(target,2):
        if t1 in edges.keys():
            if t2 in edges[t1]:
                values.add(frozenset([t_edge,t1,t2]))


print('Number of 3-cycles with a node starting with t:',len(values))
max_key = None
n_connections = -1
for edge in edges.keys():
    if n_connections < len(edges[edge]):
        max_key = edge
        n_connections = len(edges[max_key])

words = list(edges[max_key])
words.append(max_key)
words.sort()



#find all maximal full subgraphs
R = set()
P = set(edges.keys())
X = set()


find_complete_subgraphs(R,P,X,edges)

max_value = -1
max_c = None
for c in max_clusters:
    if len(c)>max_value:    
        max_value = len(c)
        max_c = c

max_c = list(max_c)
max_c.sort()

print('The password is:')
for w in max_c:
    print(w,end=",")
