class Grid():
    def __init__(self):
        self.col = 0
        self.row = 0
        self.grid : list[list[int]] = [[]]
        self.snakes = []
        self.n_snakes = len(self.snakes)
    
    def set_grid(self, col, row):
        self.col = col
        self.row = row

        


class Snake():
    def __init__(self):
        self.len = 0
        self.body = [] # list of segment's values
        self.value = 0 # total value of the snake
        self.start = () # tuple (x,y) - start position
        self.moves = []
    
    def set_len(self, len):
        self.len = len
    
    def set_start(self, start):
        self.start = start
    
    def set_moves(self, moves):
        self.moves = moves

    def calculate_value(self):
        # calculate value of snake
        for i in range(self.len):
            self.value += self.body[i]
    
    def toString(self):
        s = 

    
