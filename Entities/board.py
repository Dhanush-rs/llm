
class Board:
    
    def __init__(self,size=None):
        self.size = size
        self.board = [[]]
        self.value = None
        
    def get_size(self):
        return self.size
    
    def set_size(self, size):
        self.size=size
        
    def get_board(self):
        for char in self.board:
            print(*char,end="\n\n")

    
    def set_board(self):
        char="_"
        self.board= [ [char]*self.size for position in range(self.size)]
            
    def update_board(self, value, position):
        assert(value in ["X","O"])
        row, column = position[0],position[1]
        self.validate(row, column)
        self.board[row][column]=value
        
    def validate(self, row, column):
        if self.board[row][column]=="_" and row<self.size and column < self.size:
            return True
        raise ValueError("Invalid input")

    def check_win(self):
        for row in range(self.size):
            if self.grid[row][0] != '-' and self.grid[row][0] == self.grid[row][1] == self.grid[row][2]:
                return True

        # Check columns
        for col in range(self.size):
            if self.grid[0][col] != '-' and self.grid[0][col] == self.grid[1][col] == self.grid[2][col]:
                return True

        # Check diagonals
        if self.grid[0][0] != '-' and self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return True
        return self.grid[0][2] != '-' and self.grid[0][2] == self.grid[1][1] == self.grid[2][0]
        
