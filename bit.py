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

    print(snakes_sorted)
    for k, i in enumerate(g.snakes):
        if k < len(row_clean_indx):
            if i < g.col:
                choosen.append(i)
        else:
            break

    print(choosen)
    print(f"len coosen: {len(choosen)}")

    choosen_indexes = []
    for snake_len in choosen:
        l = list(tmp[snake_len])
        act_indx = l.pop()
        choosen_indexes.append(act_indx)
        tmp[snake_len] = set(l)

    #choosen_indexes.sort()
    print(choosen_indexes)

    res_res = ["" for i in range(0, len(g.snakes))]

    res_list = []
    indx_row_clean = 0
    indx_choosen_index = 0
    for snake_len in choosen:
        #print(f"index: {tmp[snake_len].pop()}")
        res = f"0 {row_clean_indx[indx_row_clean]}"

        for i in range(0,snake_len-1):
            res += " R"

        indx_row_clean += 1
        res_res[choosen_indexes[indx_choosen_index]] = res
        indx_choosen_index += 1
        #res_list.append(res)

    f = open("solution.txt", "w")

    for i in res_res:
        f.write(i + "\n")


g: Grid = parse_input("input/05.txt")
fill_greedy(g)