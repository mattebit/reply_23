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
    value: int = 0
    start: tuple[int, int] = ()
    moves: list[str] = []
    index: int


    def __init__(self, len, index):
        self.len = len
        self.value = 0 # total value of the snake
        self.start = () # tuple (x,y) - start position
        self.moves = []
        self.index = index


    def get_body(self, moves):
        # set body of snake based on moves
        # self.body = [self.start] -> not needed 'cause it's already in the moves list

        body = [()] # list[tuple[int, int]] = [] - list of segment's coordinates
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
            body.append((x,y))
        return body


    def calculate_value(self, g : Grid, body : list[tuple[int, int]]):
        # calculate value of snake
        for i in range(self.len):
            self.value += g.grid[body[i][0]][body[i][1]]
    

    def __str__(self):
        s = ""
        if self.start != ():
            s += f"{self.start[0]} {self.start[1]}"
            for i in self.moves:
                if i == 0:
                    s += f"{i}"
                else:
                    s += f" {i}"

        s += "\n"
        return s

