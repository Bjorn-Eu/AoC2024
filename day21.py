
#The shortest path is the shortest at each step
#hence only depending in which order we do the operations
def safe_add(coord,pos,item):
    if pos in coord.keys():
        coord[pos].add(item)
    else:
        coord[pos] = set()
        coord[pos].add(item)

#all possible paths
def get_all_paths(position,target,keypad):
    cur_pos = keypad[position] #stores (y, x)
    tar_pos = keypad[target]

    coords = {}
    coords[cur_pos] = set()
    coords[cur_pos].add('')

    while not (tar_pos in coords.keys()):
        new_coords = {}
        for p in coords.keys():
            y = p[0]
            x = p[1]
            steps = step(p,tar_pos,keypad)
            for s in steps:
                if s == '<':
                    for s2 in coords[p]:
                        safe_add(new_coords,(y,x-1),s2+s)            
                elif s == '>':
                    for s2 in coords[p]:
                        safe_add(new_coords,(y,x+1),s2+s) 
                elif s == 'v':
                    for s2 in coords[p]:
                        safe_add(new_coords,(y+1,x),s2+s) 
                elif s == '^':
                    for s2 in coords[p]:
                        safe_add(new_coords,(y-1,x),s2+s) 
        coords = new_coords
        

    
    return coords[tar_pos]

#position and target should be if the format (y, x)
def step(cur_pos,tar_pos,keypad):
    y = cur_pos[0]
    x = cur_pos[1]
    targety = tar_pos[0]
    targetx = tar_pos[1]

    new_positions = set()
    if x < targetx:
        if (y,x+1) in keypad.values():
            new_positions.add('>')
    if y < targety:
        if (y+1,x) in keypad.values():
            new_positions.add('v')
    if x>targetx:
        if (y,x-1) in keypad.values():
            new_positions.add('<')
    if y>targety:
        if (y-1,x) in keypad.values():
            new_positions.add('^')
    return new_positions


#we are interested in two things. Shortest way to type path from A to arrow (<,>,v,^)
#and correspondingly for the reverse direction
#in fact as we always start at A and need to go back to A the question is the shortest path
# A -> target -> A
def find_shortest(position,target,keypad):
    paths = get_all_paths(position,target,keypad)
    best_paths = {}
    for p in paths:
        pos = 'A'
        for c in p:
            new_paths = set()
            for path in paths2:
                #print('We got these paths back: ',get_all_paths2(pos,c,keypad2))
                for item in get_all_paths(pos,c,keypad2):
                    new_paths.add(path+item+'A')
            pos = c
            paths2 = new_paths
        
        all_paths2.update(paths2)



def fast_path(target):
    if target == 'A':
        return ''
    if target == '<':
        return 'v<<'
    if target == 'v':
        return 'v<'
    if target == '>':
        return 'v'
    if target == '^':
        return '<'
    
def fast_path2(current):
    if current == 'A':
        return ''
    if current == '^':
        return '>'
    if current == '>':
        return '^'
    if current == 'v':
        return '>^'
    if current == '<':
        return '>>^'
    else:
        print('This is impossible')

def find_optimal_path(path):
    new_path = ''
    current = 'A'
    for p in path:
        if p == 'A':
            new_path += fast_path2(current)+'A'
        else:
            new_path += fast_path(p)+'A'
        current = p
    return new_path

f = open('data\\day21.txt')
data = f.read().split()

keypad1 = {'7' : (0,0), '8':(0,1), '9':(0,2),
'4':(1,0),'5':(1,1),'6':(1,2),
'1':(2,0),'2':(2,1),'3':(2,2),
'0':(3,1),'A':(3,2)
 }

keypad2 = {'^':(0,1),'A':(0,2),'<':(1,0),'v':(1,1),'>':(1,2)}

sum = 0
for code in data:
    paths = set()
    paths.add('')
    pos = 'A'

    for c in code:
        print('We are considering position: ',pos)
        new_paths = set()
        for path in paths:
            #print('We got these paths back: ',get_all_paths2(pos,c,keypad1))
            for item in get_all_paths(pos,c,keypad1):
                new_paths.add(path+item+'A')
        pos = c
        paths = new_paths

    #print('We got the paths: ',paths)



    all_paths2 = set()
    for p in paths:
        paths2 = set()
        paths2.add('')
        pos = 'A'

        for c in p:
            #print('We are considering position: ',pos)
            new_paths = set()
            for path in paths2:
                #print('We got these paths back: ',get_all_paths2(pos,c,keypad2))
                for item in get_all_paths(pos,c,keypad2):
                    new_paths.add(path+item+'A')
            pos = c
            paths2 = new_paths
        
        all_paths2.update(paths2)


    min_length = len(min(all_paths2,key=len))
    min_paths2 = [path for path in all_paths2 if len(path)==min_length]



    all_paths2 = set()
    for p in min_paths2:
        paths2 = set()
        paths2.add('')
        pos = 'A'

        for c in p:
            new_paths = set()
            for path in paths2:
                for item in get_all_paths(pos,c,keypad2):
                    new_paths.add(path+item+'A')
            pos = c
            paths2 = new_paths
        
        all_paths2.update(paths2)

    print('Max:',len(max(all_paths2,key=len)))
    print('Min:',len(min(all_paths2,key=len)))
    print('code value: ',int(code[0:3])*len(min(all_paths2,key=len)))
    sum += int(code[0:3])*len(min(all_paths2,key=len))

print('The total sum is: ',sum)

