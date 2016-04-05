from piece import *
import sys
class Bishop(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "bishop"
        self.score = 120
    def move(self):
        y = self.y
        x = self.x

        if (y > 0 and x > 0):
            self.moveUpLeft()
        if (y > 0 and x < 10):
            self.moveUpRight()
        if (y < 10 and x > 0):
            self.moveDownLeft()
        if (y < 10 and x < 10):
            self.moveDownRight()

    def moveUpLeft(self):
    	x = self.x;
    	y = self.y

    	j = x - 1

        for i in reversed(range(y)):
            self.legalMoves.append((i,j))

            if (j == 0):
                break;
            else:
                j-=1;

    def moveUpRight(self):
    	x = self.x;
    	y = self.y

    	i = y - 1
    	j = x + 1

        for i in reversed(range(y)):
            self.legalMoves.append((i,j))

            if (j == 10):
                break;
            else:
                j+=1;

    def moveDownLeft(self):
    	x = self.x;
    	y = self.y

    	i = y + 1
    	j = x - 1

        for i in range(y + 1, 11):
            self.legalMoves.append((i,j))

            if (j == 0):
                break;
            else:
                j-=1;

    def moveDownRight(self):
    	x = self.x;
    	y = self.y

    	i = y + 1
    	j = x + 1

        for i in range(y + 1, 11):
            self.legalMoves.append((i,j))

            if (j == 10):
                break;
            else:
                j+=1;
