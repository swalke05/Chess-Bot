from piece import *;
class Pawn(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "pawn"
        self.score = 40

    def move(self):
    	y = self.y
    	x = self.x

    	if (self.inHomeRow() == True):     #Move 2 spaces forward if first move
    	    self.moveTwo()

        if (self.colour == "white" and y < 10):
    	    self.legalMoves.append((y+1,x))
    	    if (x > 0): 
                self.legalMoves.append((y+1,x-1))   #Space on downLeft square is 
    		if (x < 10): #Space on downRight square is full
    		    self.legalMoves.append((y+1,x+1))

    	elif (self.colour == "black" and y > 0):
    		self.legalMoves.append((y-1,x))
    		if (x > 0): 
    			self.legalMoves.append((y-1,x-1));
    		if (x < 10): #Space on downRight square is full
    			self.legalMoves.append((y-1,x+1))

    def moveTwo(self):
    	x = self.x;
    	y = self.y;

    	if (self.colour == "white"):
    		self.legalMoves.append((y+2, x))

    	elif (self.colour == "black"):
    		self.legalMoves.append((y-2, x))

    def inHomeRow(self):
        if (self.colour == "white"):
            if (self.y == 1):
                return True;
        elif (self.colour == "black"):
            if (self.y == 9):
                return True;
        else:
            return False;
