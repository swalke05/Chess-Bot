from piece import *;
class Serpent(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "serpent"
        self.isPoisoned = False
        self.score = 400

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
                self.legalMoves.append((y,i))

    def moveDown(self):
        y = self.y + 1
        x = self.x

        for i in range (x-1, x+2):
            if (i >= 0 and i <= 10):
                self.legalMoves.append((y,i))

    def moveLeft(self):
        y = self.y
        x = self.x

        self.legalMoves.append((y,x-1))

    def moveRight(self):
        y = self.y
        x = self.x

        self.legalMoves.append((y,x+1))

    def poison(self):
        print("poisoning!")
        y = self.y
        x = self.x

        if (y > 0):                      #poison up
            for i in range (x-1,x+2):
                if (i >= 0 and i <= 10):
                    if (board[y-1][i] != 'x' and board[y-1][i] != 'X' and board[y-1][i] != 'h' and board[y-1][i] != 'H' and self.isFriendly(board[y-1][i]) == False):
                        board[y-1][i] = '.'

        if (y < 10):                      #poison down
            for i in range (x-1,x+2):
                if (i >= 0 and i <= 10):
                    if (board[y+1][i] != 'x' and board[y+1][i] != 'X' and board[y+1][i] != 'h' and board[y+1][i] != 'H' and self.isFriendly(board[y+1][i]) == False):
                        board[y+1][i] = '.'

        if (x > 0):
            if (board[y][x-1] != 'x' and board[y][x-1] != 'X' and board[y][x-1] != 'h' and board[y][x-1] != 'H' and self.isFriendly(board[y][x-1]) == False):
                board[y][x-1] = '.'
        if (x < 10):
            if (board[y][x+1] != 'x' and board[y][x+1] != 'X' and board[y][x+1] != 'h' and board[y][x+1] != 'H' and self.isFriendly(board[y][x+1]) == False):
                board[y][x+1] = '.'