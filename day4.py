

def occurancies_of_XMAS(array):
    #find each X and count XMAS
    to_find = list('MAS')
    count = 0
    rows = len(array)
    columns = len(array[0])
    for i in range(rows):
        for j in range(columns):
            if array[i][j] == 'X': 
                #right
                if j<=columns-4:
                    arr = [array[i][j+k] for k in range(1,4)]
                    if arr == to_find:
                        count += 1
                
                #left
                if j >= 3: 
                    #print(array[i][(j-4):(j-1)])
                    arr = [array[i][j-k] for k in range(1,4)]
                    if arr == to_find:
                        count += 1
                
                #down
                if i<=rows-4:
                    arr = [array[i+k][j] for k in range(1,4)]
                    if arr == to_find:
                        count += 1
                #up
                if i>=3:
                    arr = [array[i-k][j] for k in range(1,4)]
                    if arr == to_find:
                        count += 1

                #dr
                if i<=rows-4 and j<=columns-4:
                    arr = [array[i+k][j+k] for k in range(1,4)]
                    if arr == to_find:
                        count += 1

                #dl
                if i<=rows-4 and j>= 3:
                    arr = [array[i+k][j-k] for k in range(1,4)]
                    if arr== to_find:
                        count += 1
                #ur
                if i>= 3 and j<=columns-4:
                    arr = [array[i-k][j+k] for k in range(1,4)]
                    if arr== to_find:
                        count += 1
                
                #ul
                if i>= 3 and j>=3:
                    arr = [array[i-k][j-k] for k in range(1,4)]
                    if arr== to_find:
                        count += 1
    return count    

def occurancies_of_X(array):
    #find each X and count XMAS
    to_find = list('MAS')
    count = 0
    rows = len(array)
    columns = len(array[0])
    sum = 0
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            if array[i][j] == 'A':
                arr1 = [array[i+k][j+k] for k in range(-1,2)]
                arr2 = [array[i+k][j-k] for k in range(-1,2)]
                found1 = (arr1==to_find) or (arr1 == to_find[::-1])
                found2 = (arr2==to_find) or (arr2 == to_find[::-1])
                if found1 and found2:
                    sum += 1
                 
    return sum
f = open('data/day4.txt','r')
data = f.read()
#convert to character grid
data = data.split('\n')
rows = len(data)
columns = len(data[0])
array = [[0]*columns]*rows
for i in range(rows):
        array[i] = (list(data[i]))

print('Occurancies of XMAS',occurancies_of_XMAS(array))
print('Occurancies of X-MAS',occurancies_of_X(array))






            
