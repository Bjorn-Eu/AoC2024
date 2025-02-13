
class memory:
    def __init__(disk):
        pass


#Calculate checksum of memory
def checksum(disk):
    length = len(disk)
    index = 0
    sum = 0
    while index < length:
        if disk[index] != '.':
            sum += index*int(disk[index])
        index+= 1

    return sum

#Extract full memory from input data
def extract(disk):
    array = []
    length = len(disk)//2
    odd = (len(disk)%2)!=0
    

    for i in range(length):
        t_size = disk[2*i]
        e_size = disk[2*i+1]
        for j in range(t_size):
            array.append(str(i))
        for j in range(e_size):
            array.append('.')
    #add the last memory, 
    #note input always ends with memory so checking if odd is redundant
    if odd:
        t_size = disk[2*length]
        for j in range(t_size):
            array.append(str(length))
    return array




def defrag(disk):
    p1 = 0
    p2 = len(disk)-1

    while p1<p2:
        if disk[p1]!='.':
            p1 += 1
        elif disk[p2] == '.':
            p2 -= 1
        else:
            #swap
            disk[p1],disk[p2] = disk[p2],disk[p1]

    return disk

#create a pointer to each memory together with its size
def create_pointers(disk):
    occupied_memory = []
    free_memory = []
    length = len(disk)
    index = 0
    for i in range(length//2):
        occupied_memory.append([index,disk[2*i]]) #pointer and size
        index += disk[2*i]
        free_memory.append([index,disk[2*i+1]])
        index += disk[2*i+1]

    occupied_memory.append([index,disk[length-1]])
    return occupied_memory,free_memory


#expect raw input disk
def defrag_blocks(disk):
    ext_disk = extract(disk)
    occ_mem, free_mem = create_pointers(disk)
    p2 = len(occ_mem)-1

    while 0 < p2:
        p1 = 0
        block_size = occ_mem[p2][1]
        while p1 < p2:
            if block_size <= free_mem[p1][1]:
                #swap memory blocks
                mem_ptr1 = free_mem[p1][0]
                mem_ptr2 = occ_mem[p2][0]
                ext_disk[mem_ptr1:(mem_ptr1+block_size)],ext_disk[mem_ptr2:(mem_ptr2+block_size)]=\
                ext_disk[mem_ptr2:(mem_ptr2+block_size)],ext_disk[mem_ptr1:(mem_ptr1+block_size)]
                #move file
                free_mem[p1][1] -= block_size
                free_mem[p1][0] += block_size
                break
            p1 += 1
        p2 -= 1

    return ext_disk




f = open('data/day9.txt')
data = list(map(int,f.read()))
d_disk = defrag(extract(data))

print('Checksum of memory after defrag is:',checksum(d_disk))
occ_mem, free_mem = create_pointers(data)
d_disk2 = defrag_blocks(data)
print("Checksum of memory after defrag2 is:",checksum(d_disk2))     