from time import time



def create_combinations(options,length):
    combinations = set()
    new_comb = set()
    new_comb.add("")
    while new_comb:
        to_add = set()
        for combination in new_comb:
            if len(combination) < length:
                for option in options:
                    new_str = combination + option
                    to_add.add(new_str)
        
        new_comb = to_add-combinations
        combinations.update(new_comb)
    return combinations

def is_valid(options,target):
    length = len(target)
    combinations = {} #table keeping the count to avoid reprocessing every substring
    combinations[""] = 1
    count = 0
    while combinations:
        new_candidates = {}
        for combination in combinations.keys():
            c = combinations[combination]
            for option in options:
                new_str = combination+option
                if(new_str == target):
                    count += c
                elif(len(new_str) < length) and new_str == target[0:(len(new_str))]:
                    if new_str in new_candidates.keys():
                        new_candidates[new_str] += c
                    else:
                        new_candidates[new_str] = c

        combinations = dict(new_candidates)
    return count




f = open('data/day19.txt')
data = f.read().split('\n\n')
options = data[0].split(", ")
targets = data[1].split('\n')
max_length = max([len(t) for t in targets])



valid_targets = set()
index = 0
n_comb = 0
for target in targets:
    print('Processing target',index)
    count = is_valid(options,target)
    if count>0:
        valid_targets.add(target)
        n_comb += count
    index += 1

print('The number of valid targets are: ',len(valid_targets))
print('Number of unique constructions orders are:',n_comb)

