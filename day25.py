

class T_Key:
    def __init__(self,n_pins=5,depth=7):
        self.n_pins = n_pins
        self.depth = depth
        self.pins = [-1 for _ in range(self.n_pins)]

    def increase_pin(self,index):
        self.pins[index] += 1

    def print_key(self):
        for i in range(self.n_pins):
            print(self.pins[i],end='')
        print('')


f = open('data/day25.txt')
data = (f.read()).split('\n\n')

print(data)

locksgrid= []
keysgrid = []
for d in data:
    rows = d.split()
    if d[0] == '#':
        locksgrid.append(rows)
    else:
        keysgrid.append(rows)

print('The locks are:')
print(locksgrid)
print('The keys are')
print(keysgrid)

locks = []
for lock in locksgrid:
    new_key = T_Key()
    for pin_index in range(5):
        index = 0
        while (lock[index])[pin_index]=='#':
            new_key.increase_pin(pin_index)
            index += 1
    locks.append(new_key)
    new_key.print_key()

print('Keys:')
keys = []
for key in keysgrid:
    new_key = T_Key()
    for pin_index in range(5):
        index = 6
        while (key[index])[pin_index]=='#':
            new_key.increase_pin(pin_index)
            index -= 1
    keys.append(new_key)
    new_key.print_key()

count = 0
for key in keys:
    for lock in locks:
        count += 1
        for i in range(5):
            if (key.pins[i] + lock.pins[i])>5:
                count -= 1
                break
print(count)



