import numpy as np

def print_table(table):
    row = len(table[:, 0])
    col = len(table[0, :])

    a = ord('a')
    for i in range(row):
        print(chr(a), end=' ')
        a += 1
        for j in range(col):
            print("*", end=' ')
        
        print("\n")

    for j in range(col+1):
        print(j, end=' ')



#generate coordinate system
def gen_coord(row, col):

    row_ = np.empty(row, dtype=str)
    for i in range(row):
        row_[i] = chr(97+i)
        i += 1

    col_ = np.empty(row, dtype=str) 
    for j in range(col):
        col_[j] = j+1
        j += 1

    return row_, col_




