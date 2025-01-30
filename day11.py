
import cProfile, pstats

def blink(stones):
    new_stones = set()
    n_stones = len(stones)
    for i in range(n_stones)[::-1]: #iterate backwards
        stone = stones[i]
        stone_str = (str)(stone)
        digits = len(stone_str)
        if stone == 0:
            stones[i] = 1
        elif digits%2 == 0:
                mid = digits//2
                stone1 = (int)(stone_str[0:mid])
                stone2 = (int)(stone_str[mid:digits])
                stones[i] = stone1
                stones.append(stone2) #stones.insert(i+1,stone2) #calculatioon doesnt care where we insert it..
        else:
            stones[i] = stones[i]*2024

def blink_stone(stone):
    stone_str = (str)(stone)
    digits = len(stone_str)
    if stone == 0:
        return [1]
    elif digits%2 == 0:
        mid = digits//2
        stone1 = (int)(stone_str[0:mid])
        stone2 = (int)(stone_str[mid:digits])
        return [stone1, stone2]
    else:
        return stone*2024

def tablify(stones,table = {}):
    for stone in stones:
        if stone in table.keys():
            table[stone] += 1
        else:
            table[stone] = 1
    return table

            
def blink_table(stones):
    new_stones = {}
    for stone in stones.keys(): #iterate backwards
        stone_str = (str)(stone)
        digits = len(stone_str)
        if stone == 0:
            if 1 in new_stones.keys():
                new_stones[1] += stones[stone]
            else:
                new_stones[1] = stones[stone]
        elif digits%2 == 0:
                mid = digits//2
                stone1 = (int)(stone_str[0:mid])
                stone2 = (int)(stone_str[mid:digits])
                if stone1 in new_stones.keys():
                    new_stones[stone1] += stones[stone]
                else:
                    new_stones[stone1] = stones[stone]
                if stone2 in new_stones.keys(): 
                    new_stones[stone2] += stones[stone]
                else:
                    new_stones[stone2] = stones[stone]
        else:   
            new_stone = stone*2024
            if new_stone in new_stones.keys():
                new_stones[new_stone] += stones[stone]
            else:
                new_stones[new_stone] = stones[stone]
    return new_stones
def count_number(stone,n):
    stones = [stone]
    for i in range(n):
        for s in stones:
            new_stones = blink_stone(stone)

    print(len(stones))

f = open('day11.txt','r')
stones = list(map(int,(f.read()).split()))

table = tablify(stones)
print('old stones:',table)
for i in range(75):
    table = blink_table(table)


count = 0
for stone in table.keys():
    count += table[stone]

print('total number of stones is',count)








