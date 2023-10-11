def check_board(minefield):
    for x in minefield:
        if not len(x) == len(minefield[0]):
            raise ValueError("The board is invalid with current input.")
        for ch in x:
            if ch != ' ' and ch != '*':
                raise ValueError("The board is invalid with current input.")


def count_neighbor_mines(minefield, row_number, column_number):
    mines = 0
    if minefield[row_number][column_number] == "*":
        return "*"
    for i in range(row_number - 1, row_number + 2):
        for j in range(column_number - 1, column_number + 2):
            if i >= 0 and i < len(minefield) and j >= 0 and j < len(minefield[0]) \
                      and minefield[i][j] == "*":
                mines += 1 
    return str(mines) if mines != 0 else " "


def annotate(minefield):
    if minefield == [] or minefield == ['']:
        return minefield
    check_board(minefield)
    rows = []
    for i, row in enumerate(minefield):
        cols = ''
        for j in row:
            cols += count_neighbor_mines(minefield, i, j)
        rows + cols
    
    return rows
