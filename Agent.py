import numpy as np
import colors as color
import Environment as Board
from collections import deque
class Node:
    def __init__(self, x,y):
        self.x = x
        self.y = y
class Agent:
    a=np.load("Maze.npy")
    start=0,6
    end=12,0
    func =[]
    path_so_far=[]
    b=np.load("Maze.npy")
    # board = Board(start, end)
    def __init__(self, board):
        self.position = board.get_agent_pos()
        self.current_state = board.get_current_state()
        self.gameBoard=board

    def get_position(self):
        return self.position

    def set_position(self, position, board):
        self.position = position
        board.set_agent_pos(position)
        board.update_board(self.current_state)

    def percept(self, board):
        # perception :
        # sets the current state
        # Use get_current_state function to get the maze matrix. - make your state
        self.current_state = board.get_current_state()

        pass

    # def move(self, direction):
    #     # make your next move based on your perception
    #     # check if the move destination is not blocked
    #     # if not blocked:
    #     # use red color to show visited tiles.
    #     # something like :
    #     current_pos = self.get_position()
    #     x, y = current_pos[0], current_pos[1]
    #     board.colorize(x, y, color.red)
        
    #     # then move to destination - set new position
    #     # something like :
    #     self.set_position(self.get_position() + direction)

    #     pass

    @staticmethod
    def get_actions():
        actions = []
        # returns a list of valid actions
        return actions

    def bfs(self):
        # self.percept(environment)
        # now go on !
        
        for i in range(len(self.a)):
            self.func.append([])
            for j in range(len(self.a[i])):
                self.func[-1].append(0)
        i,j = self.start
        self.func[i][j] = 1
        counter=0
        k = 0
        while self.func[0][12] == 0:
           
            k += 1
            for i in range(len(self.func)):
                for j in range(len(self.func[i])):
                    if self.func[j][i] == k:
                        if j>0 and self.func[j-1][i] == 0 and self.a[j-1][i] == 1:
                            self.func[j-1][i] = k + 1
                        if i>0 and self.func[j][i-1] == 0 and self.a[j][i-1] == 1:
                            self.func[j][i-1] = k + 1
                        if j<len(self.func)-1 and self.func[j+1][i] == 0 and self.a[j+1][i] == 1:
                            self.func[j+1][i] = k + 1
                        if i<len(self.func[i])-1 and self.func[j][i+1] == 0 and self.a[j][i+1] == 1:
                            self.func[j][i+1] = k + 1
                        self.gameBoard.colorize(i,j,color.green)
                        counter+=1
            
        i, j = self.end
        k = self.func[j][i]
        while k > 1:
            if j > 0 and self.func[j - 1][i] == k-1:
                j, i = j-1, i
                self.gameBoard.colorize(i, j,color.blue)
                k-=1
            elif i > 0 and self.func[j][i - 1] == k-1:
                j, i = j, i-1
                self.gameBoard.colorize(i,j,color.blue)
                k-=1
            elif j < len(self.func) - 1 and self.func[j + 1][i] == k-1:
                j, i = j+1, i
                self.gameBoard.colorize(i, j,color.blue)
                k-=1
            elif i < len(self.func[i]) - 1 and self.func[j][i + 1] == k-1:
                j, i = j, i+1
                self.gameBoard.colorize(i, j,color.blue)
                k -= 1
       

        print(counter) 
        pass


    def create_node(self,x, y):

        return Node(x,y)
    





    def dfs(self):
        b=np.load("Maze.npy")
       
        starting_point=Node(0,6)
        end_point=Node(0,12)
        adj_cell_x = [1, 0, 0, -1]
        adj_cell_y = [0, 1, -1, 0]
        m,n=(len(b),len(b))
        visited_blocks = [[False for i in range(m)]
                          for j in range(n)]
        visited_blocks[0][6] = True
        stack =deque()
        sol = starting_point
        stack.append(sol)
        neigh = 4
        counter=0
        while stack:
            current_block = stack.pop()
            # self.gameBoard.colorize(current_block.y,current_block.x,color.green)
            if current_block.x == 0 and current_block.y == 12:
                    print(counter)
                    return
           
            x_pos = current_block.x
            y_pos = current_block.y
            # print(x_pos)
            # print(y_pos)

            for i in range(neigh):
                if x_pos == len(b) - 1 and adj_cell_x[i] == 1:
                    x_pos = current_block.x
                    y_pos = current_block.y + adj_cell_y[i]
                elif y_pos == 0 and adj_cell_y[i] == -1:
                    x_pos = current_block.x + adj_cell_x[i]
                    y_pos = current_block.y
                # elif x_pos == 0 and adj_cell_x[i] == -1:
                #     x_pos = current_block.x
                #     y_pos = current_block.y + adj_cell_y[i]
                # elif y_pos == len(b)-1 and adj_cell_y[i] == 1:
                #     x_pos = current_block.x + adj_cell_x[i]
                #     y_pos = current_block.y
                
                else:
                    x_pos = current_block.x + adj_cell_x[i]
                    y_pos = current_block.y + adj_cell_y[i]
                if x_pos != 13 and x_pos != -1 and y_pos != 13 and y_pos != -1:
                    if b[x_pos][y_pos] == 1:
                        if not visited_blocks[x_pos][y_pos]:
                            visited_blocks[x_pos][y_pos] = True
                            counter+=1
                            stack.append(self.create_node(x_pos, y_pos))
                            self.gameBoard.colorize(y_pos,x_pos,color.blue)
                   
        print(counter)
        pass

    def a_star(self, environment):
        pass
