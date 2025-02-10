
class PushIt:
    def __init__(self,grid):
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

    def print_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if i==self.position_y and j==self.position_x:
                    print('@',end="")
                else:
                    print(grid[i][j],end="")
            print("")

    def box_sum(self):
        sum = 0
        for i in range(self.height):
            for j in range(self.width):
                if(self.grid[i][j] == 'O'):
                    sum += 100*i+j

        return sum
def move(grid,action):
    grid_width = len(grid[0])
    grid_height = len(grid)
    index = None
    for i in range(grid_height):
        for j in range(grid_width):
            if grid[i][j]=='@':
                index = (i,j)

    if action == '<':
        pass
    elif action == '^':
        pass
    elif action == '>':
        pass
    elif action == 'v': #only possibility so else
        pass

    print(index)

def push_it():
    pass


f = open('data/day15.txt')
data = f.read().split("\n\n")
instructions = data[1].replace('\n','')
data = data[0].split("\n")
width = len(data[0])
grid = [list(data[i]) for i in range(width)]



grid_width = len(grid[0])
grid_height = len(grid)

pushit = PushIt(grid)

for instruction in instructions:
    pushit.move(instruction)
    #print('Move:',instruction)
    #print("Y: ",pushit.position_y," X: ",pushit.position_x)
    #pushit.print_grid()
    

print('The box sum is:',pushit.box_sum())
#print("Y: ",pushit.position_y," X: ",pushit.position_x)
#pushit.print_grid()




