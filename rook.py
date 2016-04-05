from piece import *
import sys

class Rook(Piece):

    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "rook"
        self.score = 200

    def move(self):
        self.moveUp()
        self.moveDown()
        self.moveLeft()
        self.moveRight()

    def moveUp(self):
        y = self.y
        x = self.x

        i = y - 1

        for i in reversed(range(y)):
            self.legalMoves.append((i, x))
            #move = self.appendLegal(i, x)
            
            #if (move == 1 or move == -1):
                #break;

    def moveDown(self):
        y = self.y
        x = self.x

        i = y + 1

        for i in range(y + 1, 11):
            self.legalMoves.append((i, x))

    def moveLeft(self):
        y = self.y
        x = self.x

        i = x - 1

        for i in reversed(range(x)):
            self.legalMoves.append((y, i))

    def moveRight(self):
        y = self.y
        x = self.x

        i = x + 1

        for i in range(x + 1, 11):
            self.legalMoves.append((y, i))
