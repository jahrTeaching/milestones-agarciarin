from table import my_table

# TIC-TAC-TOE in terminal, just for fun

def main():
    #create table (rows, columns, n)
    table2 = my_table(3, 3, 3) 
    table2.printTable()

    i = 0
    while i < 1 and not table2.checks()[0]:
        table2.move()
        table2.printTable()

        if table2.checks()[0]:
            print("PLAYER: ", table2.checks()[1], " WINS!!!!!!!")


if __name__ == "__main__":
    main()
