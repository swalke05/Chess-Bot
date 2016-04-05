from piece import *;
class PrinceJoey(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "princejoey"
        self.isExploded = False
        self.score = 120
        
    def move(self):
        y = self.y
        x = self.x

        if (y > 0):
            self.moveUp()
        if (y < 10):
            self.moveDown()
        if (x > 0):
            self.moveLeft()
        if (x < 10):
            self.moveRight()

    def moveUp(self):
        y = self.y - 1
        x = self.x

        for i in range (x-1, x+2):
            if (i >= 0 and i <= 10):
                self.legalMoves.append((y, i))

    def moveDown(self):
        y = self.y + 1
        x = self.x

        for i in range (x-1, x+2):
            if (i >= 0 and i <= 10):
                self.legalMoves.append((y, i))

    def moveLeft(self):
        y = self.y
        x = self.x

        self.legalMoves.append((y, x-1))

    def moveRight(self):
        y = self.y
        x = self.x

        self.legalMoves.append((y, x+1))

    def explode(self):
        y = self.y
        x = self.x

        board[y][x] = '.'
        if (y > 0):                      #explode up
            for i in range (x-1,x+2):
                if (i >= 0 and i <= 10):
                    board[y-1][i] = '.'

        if (y < 10):                      #explode down
            for i in range (x-1,x+2):
                if (i >= 0 and i <= 10):
                    board[y+1][i] = '.'

        if (x > 0):
            board[y][x-1] = '.'
        if (x < 10):
            board[y][x+1] = '.'