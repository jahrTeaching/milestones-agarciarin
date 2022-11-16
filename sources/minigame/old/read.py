
def read_ter():
    print("Enter(player[letter] row[a, b, c] column[1, 2, 3])")
    l = list(str(input())) #input = (player[letter], row[a, b, c, ...], column[1, 2, 3, ...])

    pl = l[0]
    x = ord(l[1]) - 96
    y = int(l[2])

    return pl, x, y #retrun coordinates of table

