import math

class coord(object):

    def __init__(self, pl, row, col):
        if pl == 'x' or pl == 'o': #Empty or Players [*, x, o]
            self.Value = pl
        else:
            self.Value = '*'

        self.r = row
        self.c = col

    def getPl(self):
        return self.Value

    def getRow(self):
        return self.r

    def getCol(self):
        return self.c

    def getCoord(self):
        return self.getRow(), self.getCol()

    def printCoord(self):
        print("(", self.getRow(), ", ", self.getCol(), ")")

