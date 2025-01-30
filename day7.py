
def is_valid(total,arr):
    length = len(arr)

    values = set([arr[0]]) #add first element
    for i in range(1,length):
        element = arr[i]
        new_values = set()
        for v in values:
            new_values.add(element+v)
            new_values.add(element*v)
            concat = (str)(v)+(str)(element)
            new_values.add((int)(concat))
        values = new_values

    if total in values:
        return True
    else:
        return False





f = open('day7.txt','r')
data = f.read().split()
array = []

totals = []
values = []
new_values = []
#clean data
for d in data:
    if ':' in d:
        totals.append((int)(d[0:-1])) #remove :
        if new_values:
            values.append(new_values)
            new_values = []
    else:
        new_values.append((int)(d))

values.append(new_values) #append last values

cal_sum = 0
for total,arr in zip(totals,values):
    if is_valid(total,arr):
        cal_sum += total

print('The total calibration sum is:',cal_sum) 
