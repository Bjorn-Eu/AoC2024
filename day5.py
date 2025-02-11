import re




def good_row(row,rules):
    occured = set()
    for x in row:
        if x in occured:
            return False
        if x in rules.keys():
            occured.update(rules[x])
    return True

        

#selection sort seems appropriate?
def sort_row(row,rules):
    for i in range(100): #our sort doesnt perfectly sort.. :(.. this gets around it by sorting enough times
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

value = 0
for row in acceptable_rows:
    mid = len(row)//2
    value += (int)(row[mid])

print('The sum is',value)

#print('row_data',row_data[3])
value = 0
for row in row_data:
    if not row in acceptable_rows:
        row = sort_row(row,rules)
        mid = len(row)//2
        value += (int)(row[mid])


print('The adjusted sum is',value)





