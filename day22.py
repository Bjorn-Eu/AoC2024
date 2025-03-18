from collections import deque

def next_number(number):
    number = mix(64*number,number)
    number = prune(number)
    number = mix(number//32,number)
    number = prune(number)
    number = mix(number*2048,number)
    number = prune(number)
    return number
    
def mix(value,n):
    return value^n

def prune(n):
    return n%16777216

def get_change(values,value):
    change = []
    for i in range(1,len(values)):
        change.append(values[i]-values[i-1])

    change.append(value-values[len(values)-1])
    return change



f = open('data/day22.txt')
data = list(map(int,f.read().split()))

length = len(data)
values = {}

numbers = [[] for _ in range(length)]

sum = 0
for n in range(length):
    number = data[n]
    numbers[n].append(number%10)
    for i in range(2000):
        number = next_number(number)
        price = number%10
        numbers[n].append(price)
    
    sum += number

print('Sum of secret numbers:',sum)


#part II
N_sequences = []
seq = deque()
for n in range(0,length):
    N_sequences.append({})
    sequences = N_sequences[n]
    seq = deque()
    #add the first 4
    seq.append((numbers[n])[0])
    seq.append((numbers[n])[1])
    seq.append((numbers[n])[2])
    seq.append((numbers[n])[3])

    for index in range(4,len(numbers[n])):
        value = (numbers[n])[index]

        tup = tuple(get_change(tuple(seq),value))
        if tup in sequences.keys():
            pass
            #sequences[tup] += value
        else:
            sequences[tup] = value
        seq.popleft()
        seq.append(value)


sequences = {}
for n in range(length):
    for key in N_sequences[n]:
        if key in sequences.keys():
            sequences[key] += (N_sequences[n])[key]
        else:
            sequences[key] = (N_sequences[n])[key]
max_index = max(sequences,key=sequences.get)

print('Maximum number of bananas:',sequences[max_index])
