class Piece(object):

    def __init__(self, y, x, colour, letter):
        self.y = y
        self.x = x
        self.colour = colour
        self.legalMoves = []
        self.adjacent = []
        self.letter = letter
        self.type = ''
        self.isParalyzed = False
        self.isBiological = True
        

    def appendLegal(self, letter, y, x):
        if (isPiece(letter) == False):         #Move into empty square
            self.legalMoves.append((y,x))
            return 0

        elif (self.isHostile(letter) == True): #Move captures opponent's piece
            self.legalMoves.append((y,x))
            return 1
        else:
            return -1;                         #Illegal move                     

        return False

    def isHostile(self, piece):
        if (self.colour == 'white'):
            if (piece.colour == "white"):
                return False

        elif (self.colour == 'black'):
            if (piece.colour == "black"):
                return False

        return True

def isPiece(letter):
    if (isinstance(letter, Piece)):
        return True
    else:
        return False
    #if (inspect.isclass(letter)):
        #print ("is class")
    # if (letter == '.' or letter == '#' or letter == '*'):
    #     return False
    # else:
    #     return True
def toPiece(letter):
    if (letter == '.' or letter == '#' or letter == '*'):
        return False
    else:
        return True


