

def occurancies_of_XMAS(array):
    print(array)
    #find each X and count XMAS
    to_find = list('MAS')
    count = 0
    rows = len(array)
    columns = len(array[0])
    print('ROws',rows,'Columns',columns)
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
                    print(i,j)
                    arr = [array[i+k][j] for k in range(1,4)]
                    print(arr)
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


            
f = open('sample4.txt','r')
data = f.read()
print(data)
#convert to character grid
data = data.split('\n')
#print(data)
rows = len(data)
columns = len(data[0])
#print(data)
print(rows,columns)
array = [[0]*columns]*rows
for i in range(rows):
        array[i] = (list(data[i]))

print('Occurancies of XMAS',occurancies_of_XMAS(array))
#3 right
#2 left
#1 down
#2 up
#1 dl
#1 dr
#4 ur
#4 ul





            
