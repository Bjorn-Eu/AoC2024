#check if an array of integers is strictly monotone with stepsize <= 3
def is_safe(data):
    length = len(data)
    if length == 1:
        return True
    increasing = (data[0] < data[1])
    for i in range(length-1):
        if increasing:
            if data[i] >= data[i+1]: #check if decreasing
                return False
            if (data[i]+3) < data[i+1]: #stepsize <=3
                return False
        else:
            if data[i] <= data[i+1]: #check if increasing
                return False
            if data[i] > (data[i+1]+3): #stepsize <= 3
                return False
    return True

#checks if an array can be made safe by removing one element
def is_safe_with_dampen(data):
    if is_safe(data):
        return True
    else:
        for i in range(len(data)): 
            data_i = data[0:i]+data[(i+1):len(data)]
            if is_safe(data_i):
                return True
    return False




#read input
f = open("day2.txt", "r")
a = []
for d in f:
    data = list(map(int,d.split()))
    a.append(data)


#calculate number of safe data
count = 0
for d in a:
    #print(is_safe(d))
    if is_safe(d):
        count += 1
print(count)

count = 0
for d in a:
    if is_safe_with_dampen(d):
        count += 1

print(count)
    



