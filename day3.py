import re
f = open("data/day3.txt", "r")
data = f.read()

#part I
#matching instructions
valid_data = re.findall('mul\\(\\d+,\\d+\\)',data)

#multiply
value = 0
for d in valid_data:
        mul = list(map(int,re.findall('\\d+',d)))
        value += mul[0]*mul[1]
print('The value is:',value)


#part II
#matching instructions part II
valid_data = re.findall('mul\\(\\d+,\\d+\\)|do\\(\\)|don\'t\\(\\)',data)

#multiply
enabled = True
value = 0
for d in valid_data:
    if d == 'do()':
        enabled = True
    elif d=='don\'t()':
        enabled = False
    elif enabled:
        mul = list(map(int,re.findall('\\d+',d)))
        value += mul[0]*mul[1]
print('The value is:',value)