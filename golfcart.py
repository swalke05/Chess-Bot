from piece import *;
class GolfCart(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "golfcart"
        self.isCharged = False;
        self.isBiological = False
        self.score = 160

    def move(self):
        y = self.y
        x = self.x

        if (x > 0):
            self.moveLeft()
        if (x < 10):
            self.moveRight()

    def moveLeft(self):
        y = self.y
        x = self.x

        self.legalMoves.append((y, x-1))

    def moveRight(self):
        y = self.y
        x = self.x

        self.legalMoves.append((y, x+1))

    def charge(self):
        x = self.x
        y = self.y

        for i in range (0,11):
            board[i][self.x] = '.'
        if (y == 0):
            board[10][self.x] = self.letter
        elif (y == 10):
            board[0][self.x] = self.letter


