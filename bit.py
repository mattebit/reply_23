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
    #row_clean_indx = [str(i) for i in range(0, g.row)]
    print(f"clean rows: {len(row_clean_indx)}")
    print(f"{g.col}")

    snakes_arr : list[Snake] = []

    for k, i in enumerate(g.snakes):
        snakes_arr.append(Snake(
					i, k
				))
    #print([i.len for i in snakes_arr])
    snakes_arr.sort(reverse=True,key=lambda sn: sn.len)
    #print([i.len for i in snakes_arr])

    row_remaining = []
    c =0
    for k, s in enumerate(snakes_arr):
        if k < len(row_clean_indx):
            #print(f"{g.col-s.len}")
            if s.len < g.col:
                scarto = g.col-s.index

                pos_max = 0
                sum_max = 0
                for pos in range(0, g.col-s.len):
                    act_sum = sum(g.grid[k][pos:])
                    if act_sum > sum_max:
                        pos_max = pos
                        sum_max = act_sum

                s.start = (pos_max, row_clean_indx[k])
                c += 1

                for i in range(0, s.len - 1):
                    s.moves.append("R")
        else:
            break
    print(c)

    #print(scarto)

    snakes_arr.sort(reverse=False, key=lambda sn: sn.index)


    f = open("solution.txt", "w")

    c = 0
    for i in snakes_arr:
        #print(i.len)
        #print(i.index)
        if i.start != ():
            c +=1
        f.write(i.__str__())

    print(c)

g: Grid = parse_input("input/03.txt")
fill_greedy(g)