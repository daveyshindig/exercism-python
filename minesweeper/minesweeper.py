def annotate(minefield):
    for row in minefield:
        if len(row) != len(minefield[0]) or \
           len(row.replace(' ', '').replace('*', '')) > 0:
            raise ValueError("The board is invalid with current input.")

    