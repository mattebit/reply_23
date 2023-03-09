class Grid():
    col: int = 0
    row: int = 0
    grid: list[list[int]] = []
    occupied: list[list[bool]] = []
    snakes: list[int] = []
    n_snakes: int = 0
    score: int = 0


    def __init__(self):
        self.col = 0
        self.row = 0
        self.grid : list[list[int]]
        self.occupied: list[list[bool]]
        self.snakes = []
        self.n_snakes = len(self.snakes)
    

    def set_grid(self, col, row):
        self.col = col
        self.row = row


    def set_score(self):
        for i in range(self.n_snakes):
            self.score += self.snakes[i].value


class Snake():
    len: int = 0
    body: list[tuple[int, int]] = []
    value: int = 0
    start: tuple[int, int] = ()
    moves: list[str] = []


    def __init__(self):
        self.len = 0
        self.body = [()] # tuple(x,y) - list of segment's coordinates
        self.value = 0 # total value of the snake
        self.start = () # tuple (x,y) - start position
        self.moves = []
        
    
    def set_len(self, len):
        self.len = len
    

    def set_start(self, start):
        self.start = start
    

    def set_moves(self, moves):
        self.moves = moves

    def set_body(self, moves):
        # set body of snake based on moves
        # self.body = [self.start] -> not needed 'cause it's already in the moves list

        i = 0
        n_instructions = self.len
        while n_instructions > 0:
            if type(self.moves[i]) == int:
                x = self.moves[i]
                y = self.moves[i+1]
                i += 2
            else:
                if self.moves[i] == "U":
                    y -= 1
                elif self.moves[i] == "D":
                    y += 1
                elif self.moves[i] == "L":
                    x -= 1
                elif self.moves[i] == "R":
                    x += 1
                i += 1
            n_instructions -= 1
            self.body.append((x,y))


    def calculate_value(self, g : Grid):
        # calculate value of snake
        for i in range(self.len):
            self.value += g.grid[self.body[i][0]][self.body[i][1]]
    

    def __str__(self):
        return str(self.moves) + "\n"

    
