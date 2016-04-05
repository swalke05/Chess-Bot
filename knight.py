import sys;
from piece import *;
class Knight(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "knight";
        self.score = 120
        
    def move(self):

        y = self.y;
        x = self.x;

        if (y > 2):   #range check to not move outside the top of the board
            self.moveUp()
        if (y < 9):
            self.moveDown()
        if (x > 2):
            self.moveLeft()
        if (x < 9):
            self.moveRight()

    def moveUp(self):
        y = self.y;
        x = self.x;

        if (x > 0):
            self.legalMoves.append((y-2, x-1))
        if (x < 10):
            self.legalMoves.append((y-2, x+1))

    def moveDown(self):
        y = self.y;
        x = self.x;
        if (x > 0):
            self.legalMoves.append((y+2, x-1))
        if (x < 10):
            self.legalMoves.append((y+2, x+1)) 

    def moveLeft(self):
        y = self.y;
        x = self.x;

        if (y > 0):
            self.legalMoves.append((y-1, x-2))
        if (y < 10):
            self.legalMoves.append((y+1, x-2))

    def moveRight(self):
        y = self.y;
        x = self.x;

        if (y > 0):
            self.legalMoves.append((y-1, x+2))
        if (y < 10):
            self.legalMoves.append((y+1, x+2))




