from piece import *;
class GrandEmpress(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
    	self.type = "grandempress"
        self.isPoisoned = False
        self.score = 600
        
    def move(self):
    	y = self.y
    	x = self.x

        self.moveUp()
        self.moveDown()
        self.moveLeft()
        self.moveRight()

        if (y > 0 and x > 0):
    		self.moveUpLeft()
    	if (y > 0 and x < 10):
    		self.moveUpRight()
    	if (y < 10 and x > 0):
    		self.moveDownLeft()
    	if (y < 10 and x < 10):
    		self.moveDownRight()

        if (y > 1):              
            self.kMoveUp()
        if (y < 9):
            self.kMoveDown()
        if (x > 1):
            self.kMoveLeft()
        if (x < 9):
            self.kMoveRight()

    def moveUp(self):
        y = self.y
        x = self.x

        i = y - 1

        for i in reversed(range(y)):
            self.legalMoves.append((i,x))

    def moveDown(self):
        y = self.y
        x = self.x

        i = y + 1

        for i in range(y + 1, 11):
            self.legalMoves.append((i,x))

    def moveLeft(self):
        y = self.y
        x = self.x

        i = x - 1

        for i in reversed(range(x)):
            self.legalMoves.append((y,i))

    def moveRight(self):
        y = self.y
        x = self.x

        i = x + 1

        for i in range(x + 1, 11):
            self.legalMoves.append((y,i))

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

    def kMoveUp(self):
        y = self.y;
        x = self.x;

        if (x > 0):
            self.legalMoves.append((y-2,x-1))
        if (x < 10):
            self.legalMoves.append((y-2,x+1))

    def kMoveDown(self):
        y = self.y;
        x = self.x;
        if (x > 0):
            self.legalMoves.append((y+2,x-1))
        if (x < 10):
            self.legalMoves.append((y+2,x+1))

    def kMoveLeft(self):
        y = self.y;
        x = self.x;

        if (y > 0):
            self.legalMoves.append((y-1,x-2))
        if (y < 10):
            self.legalMoves.append((y+1,x-2))

    def kMoveRight(self):
        y = self.y;
        x = self.x;

        if (y > 0):
            self.legalMoves.append((y-1,x+2))
        if (y < 10):
            self.legalMoves.append((y+1,x+2))