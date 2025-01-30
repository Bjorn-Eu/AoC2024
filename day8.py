import itertools

def count_antinodes(data):
    columns = len(data[0])
    rows = len(data)

    #create table of each occurance
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
    
    #calculate antinodes 
    antinodes = set()
    for key in coordinates.keys():
        #find all subsets of 2 elements
        combinations = list(itertools.combinations(coordinates[key],2))
        


    return coordinates


f = open('sample8.txt','r')
data = f.read()
data = data.split()
print(data)

print(count_antinodes(data))
