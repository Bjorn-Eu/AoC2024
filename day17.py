
import re

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

    def adv(self,operand):
        self.a = (self.a)//(2**self.combo_map(operand))

    def bxl(self,operand):
        self.b = self.b^operand

    def bst(self,operand):
        self.b = self.combo_map(operand)%8
        
    def jnz(self,operand):
        #done externally
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

    def print_registry_octal(self):
        print('\nA:',oct(self.a),'B:',oct(self.b),'C:',oct(self.c))

def run_program(instructions,a=0,b=0,c=0,print=False):
    reg = Register(a,0,0)
    output = []
    length = len(instructions)
    pointer = 0
    while pointer<length:
        instruction = instructions[pointer]
        operand = instructions[pointer+1]
        pointer +=2
        if instruction == 0:
            reg.adv(operand)
        elif instruction == 1:
            reg.bxl(operand)
        elif instruction == 2:
            reg.bst(operand)
        elif instruction == 3:
            #jnz(operand)
            if reg.a != 0:
                pointer = operand
        elif instruction == 4:
            reg.bxc(operand)
        elif instruction == 5:
            output.append(reg.combo_map(operand)%8)
            if print:
                reg.out(operand)
            
        elif instruction == 6:
            reg.bdv(operand)
        elif instruction == 7:
            reg.cdv(operand)

        #reg.print_registry_octal()

    return output

f = open('data/day17.txt')
data = (f.read())
values = list(map(int,re.findall("\\d+",data)))
a = values[0]
b = values[1]
c = values[2]
instructions = values[3::]
reg =Register(a,b,c)


print('Running program, the output is:')
run_program(instructions,a=a,b=b,c=c,print=True)

index = len(instructions)-1
found_values = {}
base_sums = set()
base_sums.add(0)

all_solutions = set()
while index >= 0:
    new_base_sums = set()
    for base_sum in base_sums:
        for i in range(1,8):
            k = i*(8**index)+base_sum
            out = run_program(instructions,a=k)
            if out[index] == instructions[index]:
                
                new_base_sums.add(k)
                if (index == 0):
                    all_solutions.add(k)
    index -= 1
    base_sums = new_base_sums


print('')
print('All solutions found are:',all_solutions)
print('Minimum solution is:',min(all_solutions))