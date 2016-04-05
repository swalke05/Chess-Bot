from piece import *;
class OldWoman(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "oldwoman"
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