from parser_input import *
from data import Grid

def find_row_no_wormhole(g: Grid):
    res = []
    for i, row in enumerate(g.grid):
        has_wormhole = False
        for elem in row:
            if elem == -1:
                has_wormhole = True
        if not has_wormhole:
            res.append(i)
    return res

def fill_greedy(g: Grid):
    row_clean_indx = find_row_no_wormhole(g)
    print(f"clean rows: {len(row_clean_indx)}")

    tmp: dict[int, set[int]] = {} #size : all indexes
    for k, s in enumerate(g.snakes):
        try:
            tmp[s].add(k)
        except KeyError:
            tmp[s] = set()
            tmp[s].add(k)
    snakes_sorted = g.snakes
    snakes_sorted.sort(reverse=True)

    choosen = []

    print(f"{g.col}")

    for i in g.snakes:
        if i <= g.col:
            choosen.append(i)

    #print(choosen)

    choosen_indexes = []
    for snake_len in choosen:
        l = list(tmp[snake_len])
        choosen_indexes.append(l.pop())
        tmp[snake_len] = set(l)

    choosen_indexes.sort()
    print(choosen_indexes)

    res_list = []
    indx_row_clean = 0
    for snake_len in choosen:
        #print(f"index: {tmp[snake_len].pop()}")
        res = f"0 {indx_row_clean} "

        for i in range(0,snake_len):
            res += "R"

        print(res)
        indx_row_clean += 1
        res_list.append(res)

    f = open("solution.txt", "w")

    for i in res_list:
        f.write(i + "\n")

    missing =  len(g.snakes) - len(res_list)

    for i in range(0, missing):
        f.write("\n")



g: Grid = parse_input("input/02.txt")
fill_greedy(g)