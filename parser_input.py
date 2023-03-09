import re
from data import Grid, Snake
# First row:
#C R S
# C number of columns
# R number of rows
# S number of snakes available

# Second row
# length length ..

def parse_input(filename: str) -> Grid:
    f = open(filename)
    lines : list[str] = f.readlines()
    
    pattern_first = "(\d*)\s(\d*)\s(\d*)\n"
    # first line
    m = re.match(pattern_first, lines[0])
    res = m.group()

    c = int(m.group(1))
    r = int(m.group(2))
    s = int(m.group(3))
    print(f"c:{c} r:{r} s:{s}")

    snakes_len = []

    # second
    second = lines[1][0:-1]
    splitted_second = second.split(" ")
    assert len(splitted_second) == s
    for i in splitted_second:
        snakes_len.append(int(i))
    
    g = Grid()
    g.col = c
    g.row = r
    g.snakes = snakes_len

    # others
    for line in lines[2:]:
        line = line[0:-1]
        splitted = line.split(" ")
        row = []
        for i in splitted:
            if i == "*":
                row.append(-1)
            else:
                row.append(int(i))

        g.grid.append(row)    

    return g

#parse_input("input/05-input-opposite-points-holes.txt")

print("done")