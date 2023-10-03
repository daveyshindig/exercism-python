import re

def is_valid(isbn):
    i = 10
    x = 0
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    if isbn.find('X') >= 0 and isbn.index('X') < 9:
        return False

    for c in isbn:
        match = re.search(r'[0-9X]', c)
        if not match:
            return False

        if c == 'X':
            c = 10
        else:
            c = int(c)

        x += i * c
        i = i - 1

    return x % 11 == 0
