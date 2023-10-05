def count_neighbor_mines(minefield, row_number, column_number):
    mines = 0
    if minefield[row_number][column_number] == "*":
        return "*"
    for i in range(row_number - 1, row_number + 2):
        for j in range(column_number - 1, column_number + 2):
            if i >= 0 and i < len(minefield) and j >= 0 and j < len(minefield[0]) \
                      and minefield[i][j] == "*":
                mines += 1 
    return str(mines)


def annotate(minefield):
    rows = range(0, len(minefield))
    cols = range(0, len(minefield[0]))
    return [[count_neighbor_mines(minefield, i, j) for j in rows] for i in cols]
