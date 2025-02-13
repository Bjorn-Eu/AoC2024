import itertools

def antinode(t1,t2):
    return (2*t1[0]-t2[0],2*t1[1]-t2[1])

#finds nodes on a straight line (assumed to not be inbetween the two nodes t1 and t2)
def find_antinodes(t1,t2):
    nodes = []
    for j in range(-100,100):
        nodes.append(((1-j)*t1[0]+(j)*t2[0],(1-j)*t1[1]+(j)*t2[1]))
    return nodes

#create table of each occurance
def collect_coordinates(data):
    columns = len(data[0])
    rows = len(data)
    coordinates = {}
    for row in range(rows):
        s = data[row]
        for column in range(columns):
            char = s[column]
            if char != '.':
                if char in coordinates.keys():
                    (coordinates[char]).add((row, column))
                else:
                    coordinates[char] = set([(row, column)])
    return coordinates

def count_antinodes(coordinates,rows,columns):
    #calculate antinodes 
    antinodes = set()
    for key in coordinates.keys():
        #find all subsets of 2 elements
        combinations = list(itertools.combinations(coordinates[key],2))

        for coord in combinations:
            n1 = coord[0]
            n2 = coord[1]
            item = antinode(n1,n2)
            item2 = antinode(n2,n1)
            antinodes.add(item)
            antinodes.add(item2)

    #count antinodes
    #uncomment to print
    count = 0
    for row in range(rows):
        for column in range(columns):
            if (row,column) in antinodes:
                #print('#',end='')
                count += 1
            else:
                pass
                #print(data[row][column],end='')
        #print('')
    return count
    



def count_antinodes_resonance(coordinates,rows,columns):
    antinodes = set()
    for key in coordinates.keys():
        #find all subsets of 2 elements
        combinations = list(itertools.combinations(coordinates[key],2))

        for coord in combinations:
            n1 = coord[0]
            n2 = coord[1]
            item = find_antinodes(n1,n2)
            item2 = find_antinodes(n2,n1)
            antinodes.update(item)
            antinodes.update(item2)
    
    #count antinodes
    #uncomment to print
    count = 0
    for row in range(rows):
        for column in range(columns):
            if (row,column) in antinodes:
                #print('#',end='')
                count += 1
            else:
                pass
                #print(data[row][column],end='')
        #print('')
    return count




f = open('data/day8.txt','r')
data = f.read()
data = data.split()
rows = len(data)
columns = len(data[0])

coordinates = collect_coordinates(data)
count = count_antinodes(coordinates,rows,columns)
count2 = count_antinodes_resonance(coordinates,rows,columns)
print('The number of antinodes is:',count)
print('The number of antinodes with resonance is:',count2)
