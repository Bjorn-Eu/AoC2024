
import re
import time

class Register:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def combo_map(self,operand):
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        else:
            return operand

    #done
    def adv(self,operand):
        self.a = (self.a)//(2**self.combo_map(operand))

    #done
    def bxl(self,operand):
        self.b = self.b^operand

    #done
    def bst(self,operand):
        self.b = self.combo_map(operand)%8
        
    def jnz(self,operand):
        pass

    def bxc(self,operand):
        self.b = self.b^self.c

    def out(self,operand):
        print(self.combo_map(operand)%8,end=",")

    def bdv(self,operand):
        self.b = (self.a)//(2**self.combo_map(operand))

    def cdv(self,operand):
        self.c = (self.a)//(2**self.combo_map(operand))

    def print_registry(self):
        print('\nA:',self.a,'B:',self.b,'C:',self.c)



f = open('data/day17.txt')
data = (f.read())
values = list(map(int,re.findall("\\d+",data)))
a = values[0]
b = values[1]
c = values[2]
instructions = values[3::]
reg =Register(a,b,c)

start = time.time()
length = len(instructions)
pointer = 0
while pointer<length:
    instruction = instructions[pointer]
    operand = instructions[pointer+1]
    if instruction == 0:
        reg.adv(operand)
    elif instruction == 1:
        reg.bxl(operand)
    elif instruction == 2:
        reg.bst(operand)
    elif instruction == 3:
        #jnz(operand)
        if reg.a != 0:
            pointer = -2
    elif instruction == 4:
        reg.bxc(operand)
    elif instruction == 5:
        reg.out(operand)
    elif instruction == 6:
        reg.bdv(operand)
    elif instruction == 7:
        reg.cdv(operand)

    pointer +=2


#target = '2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0,'
