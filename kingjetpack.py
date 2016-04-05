from piece import *;
class KingJetPack(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "kingjetpack"
        self.score = 15000
        
    def move(self):
    	self.moveUpLeft()
    	self.moveUpRight()
    	self.moveDownLeft()
    	self.moveDownRight()

    def moveUpLeft(self):
    	x = self.x;
    	y = self.y

    	i = y - 1
    	j = x - 1

        for i in reversed(range(y)):
            move = self.legalMoves.append((i, j))

            if (move == 1 or move == -1):
                break;
            if (j > 0):
                j-=1;
            else:
                break

    def moveUpRight(self):
    	x = self.x;
    	y = self.y

    	i = y - 1
    	j = x + 1

        for i in reversed(range(y)):
            move = self.legalMoves.append((i, j))

            if (move == 1 or move == -1):
                break;
            if (j < 10):
                j+=1;
            else:
                break;

    def moveDownLeft(self):
    	x = self.x;
    	y = self.y

    	i = y + 1
    	j = x - 1

        for i in range(y + 1, 11):
            move = self.legalMoves.append((i, j))

            if (move == 1 or move == -1):
                break;
            if (j > 0):
            	j-=1;
            else:
            	break;
    def moveDownRight(self):
    	x = self.x;
    	y = self.y

    	i = y + 1
    	j = x + 1

        for i in range(y + 1, 11):
            move = self.legalMoves.append((i, j))

            if (move == 1 or move == -1):
                break;
            if (j < 10):
            	j+=1;
            else:
            	break;