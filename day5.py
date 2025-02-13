import re

#check if a row respect the partial ordering
def good_row(row,rules):
    occured = set()
    for x in row:
        if x in occured:
            return False
        if x in rules.keys():
            occured.update(rules[x])
    return True

#create a subdictionary only keeping the order between elements occuring in row
def create_subdict(row,rules):
    rules = dict(rules) #copy
    to_remove = rules.keys()-set(row)
    to_keep = set(row)
    for r in to_remove:
        del rules[r]
    for key in rules.keys():
        rules[key] = to_keep.intersection(rules[key])

    #finally remove empty keys
    to_remove = set()
    for key in rules.keys():
        if not rules[key]:
            to_remove.add(key)

    for key in to_remove:
        del rules[key]

    return rules
     
#topological sort, 
#expect a dictionary rules that only contains order for the elements in row
def sort_row(row,rules):
    for i in range(100): #cheatsort for now
        length = len(row)
        for i in range(length-1):
            min_index = i
            if row[i] in rules.keys():
                covalues = rules[row[i]]
                for j in range(i+1,length):             
                        if row[j] in covalues:
                            min_index = j
                            if min_index in rules.keys():
                                covalues = rules[row[j]]
                            else:
                                break
                #swap
                if min_index != i:
                    row[i],row[min_index] = row[min_index],row[i]
    return row

def top_sort(row,rules):
    rules = dict(rules) #copy
    new_row = []
    unordered = []
    for r in row:
        if not (r in rules.keys()): #adds to few
            unordered.append(r)

    while unordered:
        node = unordered.pop()
        new_row.append(node)
        for key in rules.keys():
            if node in rules[key]:
                rules[key].remove(node)
                if not rules[key]:
                    unordered.append(key)
    return new_row



f = open('data/day5.txt','r')
data = f.read().split('\n\n')
rule_data = re.findall('\\d+',data[0])
len_rules = len(rule_data)
rules = {}
#create table mapping each rule (higher to lower)
for i in range(0,len_rules,2):
    if rule_data[i+1] in rules.keys():
        rules[rule_data[i+1]].add(rule_data[i])
    else:
        rules[rule_data[i+1]] = set([rule_data[i]])

#create row array
rows = data[1].split()
row_data = []
for row in rows:
    row_data.append(re.findall('\\d+',row))


#find acceptable rows
acceptable_rows = []
bad_rows = []
for row in row_data:
    if good_row(row,rules):
        acceptable_rows.append(row)
    else:
        bad_rows.append(row)

#calculate sum of middle elements
value = 0
for row in acceptable_rows:
    mid = len(row)//2
    value += (int)(row[mid])
print('The sum is',value)


#calculate sum of middle after sorting
value = 0
for row in bad_rows:
    sub_rules = create_subdict(row,rules)
    new_row = top_sort(row,sub_rules)
    mid = len(new_row)//2
    value += (int)(new_row[mid])


print('The adjusted sum is',value)





