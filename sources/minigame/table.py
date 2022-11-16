from numpy import empty

class my_table:
    
    def __init__(self, rows, cols, n):
        self.rcd = n #3-in-row/col/diag
        self.r = rows
        self.c = cols
        self.t = empty([rows, cols], dtype=str) #player

        for i in range(rows):
            for j in range(cols):
                self.t[i, j] = '*'

    def move(self): #Automatically
        pl, r, c = self.read_move()
        self.enter_move(pl, r, c)

    def enter_move(self, pl, r, c): #for manually purposes
        if (r > 0 and r <= self.r) and (c > 0 and c <= self.c):
            self.t[r-1, c-1] = pl

    def read_move(self):
        print("Enter (player[letter] row[a, b, c] column[1, 2, 3])")
        l = list(str(input())) #input = (player[letter], row[a, b, c, ...], column[1, 2, 3, ...])

        pl = l[0]
        r = ord(l[1]) - 96
        c = int(l[2])

        return pl, r, c #return coordinates of table

    def printTable(self):
        for i in range(self.c+1):
            print(i, end=' ')
        print("\n")
        
        a = ord('a')
        for j in range(self.r):
            print(chr(a), end=' ')
            a += 1
            for i in range(self.c):
                print(self.t[j, i], end=' ')

            print("\n")

        print("________________")

    
    def evaluate_v(self, v):
        a = False
        for i in range(len(v)-self.rcd+1):
            if (v[i] == v[i+1] and v[i] == v[i+2]) and v[i] != '*':
                a = True
        return a


    def check_rows(self):
        win = False      #True
        winner = '*'     #Winner
        for i in range(self.r): #all rows
            row = self.t[i, :]

            for j in range(self.c-self.rcd+1): #all potentials groups of "rcd" in the same row
                v = empty(self.rcd, dtype=str)
                for rcd_ in range(self.rcd):   
                    v[rcd_] = row[j+rcd_]   #define the vector, contains "rcd" movements to be evaluated 
                    
                if self.evaluate_v(v):
                    win = True      #True
                    winner = v[0]   #Winner
        
        return win, winner


    def check_columns(self):
        win = False      #True
        winner = '*'     #Winner
        for i in range(self.c): #all columns
            col = self.t[:, i]

            for j in range(self.r-self.rcd+1): #all potentials groups of "rcd" in the same col
                v = empty(self.rcd, dtype=str)
                for rcd_ in range(self.rcd):   
                    v[rcd_] = col[j+rcd_]   #define the vector, contains "rcd" movements to be evaluated 
                    
                if self.evaluate_v(v):
                    win = True      #True
                    winner = v[0]   #Winner
        
        return win, winner


    def look_for_v1(self, v0):
        v = empty(self.rcd, dtype=str)

        for i in range(self.rcd): #
            v[i] = self.t[v0[0]-i, v0[1]+i]

        return v

    def look_for_v2(self, v0):
        v = empty(self.rcd, dtype=str)

        for i in range(self.rcd): #
            v[i] = self.t[v0[0]-i, v0[1]-i]

        return v


    def check_diag(self):
        win = False      #True
        winner = '*'     #Winner
        for i in range(self.c-self.rcd+1): #columns

            #diagonalA
            for j in range(self.r-self.rcd+1): #rows
                v01 = [j+self.rcd-1, i] #coordinates v0
                v1 = self.look_for_v1(v01)

                if self.evaluate_v(v1):
                    win = True      #True
                    winner = v1[0]   #Winner

            #diagonalB
            for z in range(self.r-self.rcd+1): #rows
                v02 = [z+self.rcd-1, self.c-1-i] #coordinates v0
                v2 = self.look_for_v2(v02)

                if self.evaluate_v(v2):
                    win = True       #True
                    winner = v2[0]   #Winner
        
        return win, winner


    def checks(self):
        win1, winner1 = self.check_rows()
        win2, winner2 = self.check_columns()
        win3, winner3 = self.check_diag()

        if win1 or win2 or win3:
            if win1 == True:
                return win1, winner1

            if win2 == True:
                return win2, winner2
            
            if win3 == True:
                return win3, winner3
        else:
            return False, '*'
    