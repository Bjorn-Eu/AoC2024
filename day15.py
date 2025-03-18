
import copy
class PushIt:
    def __init__(self,grid):
        self.targets =set(['O','[',']'])
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.position_x = None
        self.position_y = None
        self.init_position()

    def init_position(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j]=='@':
                    self.position_x = j
                    self.position_y = i
                    self.grid[i][j] = '.'
                    return
    #part I move
    def move(self,action):
        stop = set(['#','.'])
        x_index = self.position_x
        y_index = self.position_y
        if action == '<':
            x_index -= 1
            while self.grid[y_index][x_index] not in stop:
                x_index -= 1
            
            if x_index != self.position_x and self.grid[y_index][x_index] == '.':
                #push it
                while x_index != self.position_x:
                    self.grid[y_index][x_index] = self.grid[y_index][x_index+1]
                    x_index += 1

                self.position_x -= 1         
        elif action == '>':
            x_index += 1
            while self.grid[y_index][x_index] not in stop:
                x_index += 1
            
            if self.grid[y_index][x_index] == '.':
                #push it
                while x_index != self.position_x:
                    self.grid[y_index][x_index] = self.grid[y_index][x_index-1]
                    x_index -= 1

                self.position_x +=1 
        elif action == '^':
            y_index -= 1
            while self.grid[y_index][x_index] not in stop:
                y_index -= 1

            if self.grid[y_index][x_index] == '.':
                #push it
                while y_index != self.position_y:
                    self.grid[y_index][x_index] = self.grid[y_index+1][x_index]
                    y_index += 1

                self.position_y -=1
        elif action == 'v': #only possibility so else
            y_index += 1
            while self.grid[y_index][x_index] not in stop:
                y_index += 1
            
            if self.grid[y_index][x_index] == '.':
                #push it
                while y_index != self.position_y:
                    self.grid[y_index][x_index] = self.grid[y_index-1][x_index]
                    y_index -= 1

                self.position_y +=1 

    #part II move
    def move2(self,action):
        if action == '^':
            self.shift(self.position_x,self.position_y,action)
            self.position_y -= 1
        elif action == 'v':
            self.shift(self.position_x,self.position_y,action)
            self.position_y += 1

    #part II
    def shift(self,x,y,action):
        if action == '^':
            if self.grid[y-1][x] == '.':
                self.grid[y-1][x] = self.grid[y][x]
                self.grid[y][x] = '.'
            elif self.grid[y-1][x] == '[':
                self.shift(x,y-1,action)
                self.shift(x+1,y-1,action)
                self.grid[y-1][x] = self.grid[y][x]
                self.grid[y-1][x+1] = '.'
                
            elif self.grid[y-1][x] == ']':
                self.shift(x,y-1,action)
                self.shift(x-1,y-1,action)
                self.grid[y-1][x] = self.grid[y][x]
                self.grid[y-1][x-1] = '.'

        if action == 'v':
            if self.grid[y+1][x] == '.':
                self.grid[y+1][x] = self.grid[y][x]
                self.grid[y][x] = '.'
            elif self.grid[y+1][x] == '[':
                self.shift(x,y+1,action)
                self.shift(x+1,y+1,action)
                self.grid[y+1][x] = self.grid[y][x]
                self.grid[y+1][x+1] = '.'
            elif self.grid[y+1][x] == ']':
                self.shift(x,y+1,action)
                self.shift(x-1,y+1,action)
                self.grid[y+1][x] = self.grid[y][x]
                self.grid[y+1][x-1] = '.'

    #helper function for part II
    def can_move(self,x,y,action):
        if action == '<':
            if self.grid[y][x-1] == '#':
                return False
            elif self.grid[y][x-1] == '[':
                return self.can_move(x-1,y,action)
            elif self.grid[y][x-1] == ']':
                return self.can_move(x-1,y,action)
            else:
                return True
        elif action == '>':
            if self.grid[y][x+1] == '#':
                return False
            elif self.grid[y][x+1] == '[':
                return self.can_move(x+1,y,action)
            elif self.grid[y][x+1] == ']':
                return self.can_move(x+1,y,action)
            else:
                return True
        elif action == '^':
            if self.grid[y-1][x] == '#':
                return False
            elif self.grid[y-1][x] == '[':
                return self.can_move(x,y-1,action)  and self.can_move(x+1,y-1,action)
            elif self.grid[y-1][x] == ']':
                return self.can_move(x,y-1,action)  and self.can_move(x-1,y-1,action)
            else:
                return True

        elif action == 'v':
            if self.grid[y+1][x] == '#':
                return False
            elif self.grid[y+1][x] == '[':
                return self.can_move(x,y+1,action)  and self.can_move(x+1,y+1,action)
            elif self.grid[y+1][x] == ']':
                return self.can_move(x,y+1,action)  and self.can_move(x-1,y+1,action)
            else:
                return True
            

    def print_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if i==self.position_y and j==self.position_x:
                    print('@',end="")
                else:
                    print(self.grid[i][j],end="")
            print("")

    #part I
    def box_sum(self):
        sum = 0
        for i in range(self.height):
            for j in range(self.width):
                if(self.grid[i][j] in self.targets):
                    sum += 100*i+j
        return sum

    #box sum for part II
    def box_sum2(self):
        sum = 0
        for i in range(self.height):
            for j in range(self.width):
                if(self.grid[i][j] == '['):
                    sum += 100*i+j
        return sum

#scale grid with width 2x for part II
def create_2Xgrid(grid):
    width = len(grid[0])
    height = len(grid)
    big_grid = [['.' for i in range(2*width)] for j in range(len(grid))]
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '#':
                pass
                (big_grid[y])[2*x] = '#'
                (big_grid[y])[2*x+1] = '#'
            elif grid[y][x] == 'O':
                (big_grid[y])[2*x] = '['
                (big_grid[y])[2*x+1] = ']'
            elif grid[y][x] == '@':
                (big_grid[y])[2*x] = '@'


    return big_grid

f = open('data/day15.txt')
#create grid
data = f.read().split("\n\n")
instructions = data[1].replace('\n','')
data = data[0].split("\n")
width = len(data[0])
grid = [list(data[i]) for i in range(width)]

grid2 = copy.deepcopy(grid)
pushit = PushIt(grid)

#simulate
for instruction in instructions:
    pushit.move(instruction)


pushit.print_grid()
print('The box sum is:',pushit.box_sum())


#part 2
big_grid = create_2Xgrid(grid2)

pushit = PushIt(big_grid)


pushit.print_grid()

#simulate
for instruction in instructions:
    if pushit.can_move(pushit.position_x,pushit.position_y,instruction):
        if instruction == '<' or instruction == '>':
            pushit.move(instruction)
        else:
            pushit.move2(instruction)

pushit.print_grid()
print('The box sum for big grid is:',pushit.box_sum2())





