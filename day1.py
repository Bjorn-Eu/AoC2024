#sorted difference metric between two lists
def sorted_difference(a,b):
    a.sort()
    b.sort()
    length = len(a)
    distance = 0
    for i in range(length):
        distance += abs(a[i]-b[i])
    return distance

#simalarity score
#calculates the product of occurances of a value in each array weighted by the value
def simalarity(a,b):
    table_a = {}
    for e in a:
        if e in table_a.keys():
            table_a[e] += 1
        else:
            table_a[e] = 1
    score = 0
    for e in b:
        if e in table_a.keys():
            score += e*table_a[e]
            print('once',score)

    return score


#read input
f = open("day1.txt", "r")
a = []
b = []
for d in f:
    data = d.split()
    a.append((int)(data[0]))
    b.append((int)(data[1]))

print('Difference score:',sorted_difference(a,b))

print('Similarity score:',simalarity(a,b))
