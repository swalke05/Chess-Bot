from __future__ import print_function

from piece import *
from bishop import *
from catapult import *
from golfcart import *
from gorilla import *
from grandempress import *
from king import *
from kingjetpack import *
from knight import *
from oldwoman import *
from pawn import *
from princejoey import *
from rook import *
from serpent import *
from timemachine import *
from beekeeper import *
import copy

class Board:
    def __init__(self, fileContents):
        self.currentTurn = ''

        self.whitePieces = []
        self.blackPieces = []
        self.capturedPieces = []
        self.board = []
        self.blocking = []
        self.whiteCart = None
        self.blackCart = None
        self.blackScore = 0
        self.whiteScore = 0

        self.generateState(fileContents)
                    #print(self.board[y][x].type, self.board[y][x].y, self.board[y][x].x)
    def checkFirstMove(self):
        isFirstMove = True

        if (self.currentTurn == "W"):
            for y in range(0,2):
                for x in range(0,11):
                    if (isPiece(self.board[y][x]) == False or self.board[y][x].colour == "black"):
                        isFirstMove = False

        elif (self.currentTurn == "B"):
            for y in range(9,11):
                for x in range(0,11):
                    if (isPiece(self.board[y][x]) == False or self.board[y][x].colour == "white"):
                        isFirstMove = False

        return isFirstMove


    def checkParalyzed(self, piece):
        self.getAdjacent(piece)
        for adjacentPiece in piece.adjacent:
            if (adjacentPiece.type == "beekeeper" and piece.isHostile(adjacentPiece)):
                piece.isParalyzed = True

    def movePieces(self):
        if (self.currentTurn == 'W'):
            for piece in self.whitePieces:
                self.checkParalyzed(piece)
                if (piece.type != "timemachine" and piece.isParalyzed == False):
                    piece.move()
                    self.evaluateMoves(piece)

        if (self.currentTurn == 'B'):
            for piece in self.blackPieces:
                self.checkParalyzed(piece)
                if (piece.type != "timemachine" and piece.isParalyzed == False):
                    piece.move() 
                    self.evaluateMoves(piece)


    def calculateDistanceScore(self, piece):
        distance = 0

        if (piece.colour == "black"): 
            if (piece.type == "pawn" and piece.y == 9):
                distance = -30
                self.blackScore -= 50
            else:
                distance = (10-piece.y)

        elif (piece.colour == "white"):
            if (piece.type == "pawn" and piece.y == 1):
                distance = -30
                self.whiteScore -= 50
            else:
                distance = (piece.y)

        if (piece.type == "king" and distance > 2):
            return (distance * (-10000))
        if (piece.type == "serpent"):
            return distance*40
        if (piece.type != "pawn"):
            return distance*10
        else:
            return distance


    def calculateScores(self):
        whitePieces = []
        blackPieces = [] #probably could have just used global list

        for y in range(0,11):
            for x in range(0,11):
                piece = self.board[y][x]
                if (isPiece(piece) and piece.colour == "white"):
                    whitePieces.append(piece)
                elif (isPiece(piece) and piece.colour == "black"):
                    blackPieces.append(piece)

        for piece in whitePieces:
            self.whiteScore += piece.score
            self.whiteScore += self.calculateDistanceScore(piece)
        for piece in blackPieces:
            self.blackScore += piece.score
            self.blackScore += self.calculateDistanceScore(piece)



    def toMinMaxFormat(self):
        nextFile = []
        if (self.currentTurn == 'W'):
            nextFile.append('B\n')
        elif (self.currentTurn == 'B'):
            nextFile.append('W\n')

        for y in range(0,11):
            line = ""
            for x in range(0,11):
                piece = self.board[y][x]

                if isPiece(piece):
                    line += piece.letter
                else:
                    if (y == 3 and x == 1):
                        line += "*"
                    elif (y == 3 and x == 9):
                        line += "*"
                    elif (y == 7 and x == 1):
                        line += "*"
                    elif (y == 7 and x == 9):
                        line += "*"
                    elif (y == 5 and x == 5):
                        line += "#"
                    else:
                        line += "."
            line += '\n'
            nextFile.append(line)
        nextFile.append('0')
        nextFile.append('0')
        nextFile.append('0')

        return nextFile



    def toFileFormat(self):
        if (self.currentTurn == 'W'):
            print('B')
        elif (self.currentTurn == 'B'):
            print('W')
        
        for y in range(0,11):
            for x in range(0,11):
                piece = self.board[y][x]
                if isPiece(piece):
                    print(piece.letter,end="")
                else:
                    if (y == 3 and x == 1):
                        print("*",end="")
                    elif (y == 3 and x == 9):
                        print("*",end="")
                    elif (y == 7 and x == 1):
                        print("*",end="")
                    elif (y == 7 and x == 9):
                        print("*",end="")
                    elif (y == 5 and x == 5):
                        print ("#",end="")
                    else:
                        print(".",end="")
            print ("")
        print("0")
        print("0")
        print("0")


    def checkUp(self, piece):
        y = piece.y
        x = piece.x
        blocked = False
        
        for i in reversed(range(y)):
            if (blocked == True):
                self.blocking.append((i, x))

            if (isPiece(self.board[i][x])):
                blocked = True

    def checkDown(self, piece):
        y = piece.y
        x = piece.x
        blocked = False

        for i in range(y + 1, 11):
            if (blocked == True):
                self.blocking.append((i, x))

            if (isPiece(self.board[i][x])):
                blocked = True

    def checkLeft(self, piece):
        y = piece.y
        x = piece.x
        blocked = False

        for i in reversed(range(x)):
            if (blocked == True):
                self.blocking.append((y, i))

            if (isPiece(self.board[y][i])):
                blocked = True

    def checkRight(self, piece):
        y = piece.y
        x = piece.x
        blocked = False

        #check for blocking to the right
        for i in range(x + 1, 11):
            if (blocked == True):
                self.blocking.append((y, i))

            if (isPiece(self.board[y][i])):
                blocked = True

    def checkUpLeft(self, piece):
        y = piece.y
        x = piece.x
        blocked = False

        j = x - 1

        for i in reversed(range(y)):
            if (blocked == True):
                self.blocking.append((i, j))

            if (isPiece(self.board[i][j])):
                blocked = True

            if (j == 0):
                break;
            else:
                j-=1;

    def checkUpRight(self, piece):
        y = piece.y
        x = piece.x
        blocked = False

        j = x + 1

        for i in reversed(range(y)):
            if (blocked == True):
                self.blocking.append((i, j))

            if (isPiece(self.board[i][j])):
                blocked = True

            if (j == 10):
                break;
            else:
                j+=1;

    def checkDownLeft(self, piece):
        y = piece.y
        x = piece.x
        blocked = False

        j = x - 1

        for i in range(y + 1, 11):
            if (blocked == True):
                self.blocking.append((i, j))

            if (isPiece(self.board[i][j])):
                blocked = True

            if (j == 0):
                break;
            else:
                j-=1;

    def checkDownRight(self, piece):
        y = piece.y
        x = piece.x
        blocked = False

        j = x + 1

        for i in range(y + 1, 11):
            if (blocked == True):
                self.blocking.append((i, j))

            if (isPiece(self.board[i][j])):
                blocked = True

            if (j == 10):
                break;
            else:
                j+=1;

    def determineBlocking(self, piece):
        y = piece.y
        x = piece.x
        del self.blocking[:]

        if (piece.type == "rook"):
            self.checkUp(piece)
            self.checkDown(piece)
            self.checkLeft(piece)
            self.checkRight(piece)

        elif (piece.type == "bishop" or piece.type == "kingjetpack"):
            if (y > 0 and x > 0):
                self.checkUpLeft(piece)
            if (y > 0 and x < 10):
                self.checkUpRight(piece)
            if (y < 10 and x > 0):
                self.checkDownLeft(piece)
            if (y < 10 and x < 10):
                self.checkDownRight(piece)

        elif (piece.type == "grandempress"):
            if (y > 0 and x > 0):
                self.checkUpLeft(piece)
            if (y > 0 and x < 10):
                self.checkUpRight(piece)
            if (y < 10 and x > 0):
                self.checkDownLeft(piece)
            if (y < 10 and x < 10):
                self.checkDownRight(piece)

            self.checkUp(piece)
            self.checkDown(piece)
            self.checkLeft(piece)
            self.checkRight(piece)

        elif (piece.type == "catapult"):
            for move in piece.legalMoves:
                y = move[0]
                x = move[1]

                if (isPiece(self.board[y][x])): #Catapult can't capture
                    self.blocking.append((y,x))
            #TODO figure out where i left off here

        elif (piece.type == "gorilla"):
            for move in piece.legalMoves:
                y = move[0]
                x = move[1]

                if ((x == 0 or x == 10) and x != piece.x): #Gorilla can't knock pieces off board
                    if (isPiece(self.board[y][x])):
                        self.blocking.append(move)
                if ((y == 0 or y == 10) and y != piece.y):
                    if (isPiece(self.board[y][x])):
                        self.blocking.append(move)

        elif (piece.type == "pawn"):
            for move in piece.legalMoves:
                y = move[0]
                x = move[1]

                if (x != piece.x and (isPiece(self.board[y][x]) == False)): #attacking move
                    self.blocking.append(move)

                elif (x == piece.x and (isPiece(self.board[y][x]) == True)):
                    self.blocking.append(move)

        elif (piece.type == "serpent"):
            for move in piece.legalMoves:
                y = move[0]
                x = move[1]

                if (isPiece(self.board[y][x])):     #Serpent can't capture
                    self.blocking.append(move)

    def evaluateMoves(self, piece):
        self.blocking = []
        del self.blocking[:]        #clear the blocked list

        legalMoves = []

        #if (piece.type == "rook" or piece.type == "bishop" or piece.type == "grandempress"):
           # print("moves")
            #print (piece.legalMoves)
        self.determineBlocking(piece)
           # print ("blocking")
           # print (self.blocking)

        for move in piece.legalMoves:      #Remove bad moves
            if (move not in self.blocking):
                legalMoves.append(move)

        piece.legalMoves = copy.deepcopy(legalMoves)
        del legalMoves[:]

        for move in piece.legalMoves:
            y = move[0]
            x = move[1]
            destination = self.board[y][x]

            if (isPiece(destination)):
                if (piece.isHostile(destination) == True and destination.type != "gorilla" and piece.type != "catapult"):
                    legalMoves.append(move)
                elif(piece.type == "gorilla" and destination.type != "gorilla"):
                    legalMoves.append(move)
            else:
                legalMoves.append(move)

        #print("legal moves")
        piece.legalMoves = copy.deepcopy(legalMoves)
        #print(piece.legalMoves)
        #print("\n")

    def getAdjacent(self, piece):
        y = piece.y
        x = piece.x
        del piece.adjacent[:] #Clear list of adjacent pieces

        #print (piece.type, "at", piece.y, piece.x)

        if (y > 0):
            for i in range (x-1,x+2):
                if (i >= 0 and i <= 10):
                    if (isPiece(self.board[y-1][i])):
                        piece.adjacent.append(self.board[y-1][i])
        if (y < 10):
            for i in range (x-1,x+2):
                if (i >= 0 and i <= 10):
                    if isPiece(self.board[y+1][i]):
                        piece.adjacent.append(self.board[y+1][i])

        if (x > 0):
            if (isPiece(self.board[y][x-1])):
                piece.adjacent.append(self.board[y][x-1])

        if (x < 10):
            if (isPiece(self.board[y][x+1])):
                piece.adjacent.append(self.board[y][x+1])

        #print("adjacent")
        #print(piece.adjacent)

    def removePiece(self, piece):
        if (isPiece(piece) == False):
            return

        y = piece.y
        x = piece.x

        self.capturedPieces.append(piece)
        if (piece in self.whitePieces):
            self.whitePieces.remove(piece)
        elif (piece in self.blackPieces):
            self.blackPieces.remove(piece)

        self.board[y][x] = None

    def toEmpress(self, oldwoman):
        y = oldwoman.y
        x = oldwoman.x
        colour = oldwoman.colour

        if (colour == "white"):
            empress = GrandEmpress(y, x, colour, 'E')
        elif (colour == "black"):
            empress = GrandEmpress(y, x, colour, 'e')

        self.board[y][x] = empress

    def poisonAdjacent(self, serpent):
        y = serpent.y
        x = serpent.x

        self.getAdjacent(serpent);
        for piece in serpent.adjacent:
            if (serpent.isHostile(piece) and piece.isBiological):
                self.getAdjacent(piece)
                for adjacentPiece in piece.adjacent:
                    if (adjacentPiece.type == "oldwoman" and (piece.isHostile(adjacentPiece) == False)):
                        self.toEmpress(adjacentPiece)
                        #TODO make new grand empress to replace
                if (piece.type == "serpent"):
                    serpent.isPoisoned = True
                    piece.isPoisoned = True
                else:
                    self.removePiece(piece)

    def checkSerpents(self):
        for y in range(0,11):
            for x in range (0,11):
                #if (isPiece(self.board[y][x])):
                    #print(self.board[y][x].type, " at", self.board[y][x].y, self.board[y][x].x)
                if (isPiece(self.board[y][x]) and self.board[y][x].type == "serpent"):
                    self.poisonAdjacent(self.board[y][x])
                    if (self.board[y][x].isPoisoned):
                        self.removePiece(self.board[y][x])
        for y in range(0,11):
            for x in range (0,11):
                #if (isPiece(self.board[y][x])):
                    #print(self.board[y][x].type, " at", self.board[y][x].y, self.board[y][x].x)
                if (isPiece(self.board[y][x]) and self.board[y][x].type == "grandempress"):
                    self.poisonAdjacent(self.board[y][x])
                    if (self.board[y][x].isPoisoned):
                        self.removePiece(self.board[y][x])

    def playMove(self, piece, move):
        y = piece.y
        x = piece.x

        destY = move[0]
        destX = move[1]

        self.movePiece(piece, move)

    def getDirection(self,piece, destination):
        #possibly do if statement for catapult and gorilla

        curY = piece.y
        curX = piece.x
        destY = destination[0]
        destX = destination[1]

        if (destY == curY):  #Moving horizionatally
            if (destX > curX): #Moving right
                piece.direction = "right"
            elif (destX < curX): #Moving left
                piece.direction = "left"

        elif (destX == curX): #Moving Vertically
            if (destY > curY): #Moving down
                piece.direction = "down"
            elif (destY < curY): #Moving up
                piece.direction = "up"

        elif (destY < curY): #Moving up
            if (destX > curX):
                piece.direction = "upright"
            elif (destX < curX):
                piece.direction = "upleft"
        elif (destY > curY): #Moving down
            if (destX > curX):
                piece.direction = "downright"
            elif (destX < curX):
                piece.direction = "downleft"


    def determineShove(self, piece, direction):
        y = piece.y
        x = piece.x

        if (direction == "up"):
            destination = ((y-1,x))
        elif (direction == "down"):
            destination = ((y+1,x))
        elif (direction == "left"):
            destination = ((y,x-1))
        elif (direction == "right"):
            destination = ((y,x+1))

        elif (direction == "upright"):
            destination = ((y-1,x+1))
        elif (direction == "upleft"):
            destination = ((y-1,x-1))
        elif (direction == "downright"):
            destination = ((y+1,x+1))
        elif (direction == "downleft"):
            destination = ((y+1,x-1))

        y = destination[0]
        x = destination[1]

        if (isPiece(self.board[y][x])):
            if (self.board[y][x].type != "gorilla"):
                self.movePiece(piece, destination)
            else: 
                return False
        else:
            self.movePiece(piece, destination)

    def movePiece(self, piece, destination):
        y = destination[0]
        x = destination[1]

        if (self.board[piece.y][piece.x].type == "gorilla"):
            self.getDirection(piece, destination)
            if (isPiece(self.board[y][x])):
                if (self.determineShove(self.board[y][x], piece.direction) == False):
                    return


        self.board[piece.y][piece.x] = None

        if (isPiece(self.board[y][x])):
            self.removePiece(self.board[y][x])

        self.board[y][x] = piece
        piece.y = y
        piece.x = x

    def promotePawn(self, piece):
        y = piece.y
        x = piece.x
        colour = piece.colour

        self.removePiece(piece)
        if (colour == "black"):
            timeMachine = TimeMachine(y, x, colour, 'h')
        elif(colour == "white"):
            timeMachine = TimeMachine(y, x, colour, 'H')

        self.board[y][x] = timeMachine


    def checkCarts(self):

        if (self.whiteCart not in self.whitePieces and self.blackCart not in self.blackPieces):
            return

        for x in range(0,11):
            piece = self.board[5][x]
            if (isPiece(piece) and piece.type == "pawn"):
                if (piece.colour == "white"):
                    if (self.blackCart in self.blackPieces):
                        self.blackCart.isCharged = True
                elif (piece.colour == "black"):
                    if (self.whiteCart in self.whitePieces):
                        self.whiteCart.isCharged = True

        #promote pawns
        for x in range(0,11):
            piece = self.board[0][x]
            if (isPiece(piece) and piece.colour == "black" and piece.type == "pawn"):
                self.promotePawn(piece)

        for x in range(10,11):
            piece = self.board[0][x]
            if (isPiece(piece) and piece.colour == "white" and piece.type == "pawn"):
                self.promotePawn(piece)



        y=0
        for i in range (0,2):
            for x in range(0,11):
                piece = self.board[y][x]
                if (isPiece(piece) and piece.type == "timemachine"):
                    if (piece.colour == "white"):
                        if (self.whiteCart in self.whitePieces):
                            self.whiteCart.isCharged = True
                    elif (piece.colour == "black"):
                        if (self.blackCart in self.blackPieces):
                            self.blackCart.isCharged = True
            y = 10

        if ((self.whiteCart in self.whitePieces and self.blackCart in self.blackPieces) and self.whiteCart.isCharged and self.blackCart.isCharged and self.whiteCart.x == self.blackCart.x ):

            for y in range(0,11):
                piece = self.board[y][self.whiteCart.x] #doesn't matter - same column
                self.removePiece(piece)
 
        else:
            if (self.whiteCart in self.whitePieces and self.whiteCart.isCharged):
                cart = self.whiteCart

                if (cart.y == 0):
                    destination = 10
                elif (cart.y == 10):
                    destination = 0

                if (cart.y == 0):
                    self.movePiece(cart, (10,cart.x))
                    for y in range (1,10):
                        self.removePiece(self.board[y][cart.x])

                elif (cart.y == 10):
                    self.movePiece(cart, (0,cart.x))
                    for y in reversed(range(1,11)):
                        self.removePiece(self.board[y][cart.x])


            if (self.blackCart in self.blackPieces and self.blackCart.isCharged):
                cart = self.blackCart
                if (cart.y == 0):
                    destination = 10
                elif (cart.y == 10):
                    destination = 0

                if (cart.y == 0):
                    self.movePiece(cart, (10,cart.x))
                    for y in range (1,10):
                        self.removePiece(self.board[y][cart.x])

                elif (cart.y == 10):
                    self.movePiece(cart, (0,cart.x))
                    for y in reversed(range(1,11)):
                        self.removePiece(self.board[y][cart.x])

    def poisonRoundTwo(self, transported):
        for piece in transported:
            y = piece.y
            x = piece.x
            if (piece.type == "serpent" or piece.type == "grandempress"):
                self.poisonAdjacent(piece)
                if (piece.isPoisoned):
                    self.removePiece(self.board[y][x])
            else:
                self.getAdjacent(piece)
                for adjacentPiece in piece.adjacent:
                    if ((adjacentPiece.type == "serpent" or adjacentPiece.type == "grandempress") and piece.isHostile(adjacentPiece) and piece.isBiological):
                        self.removePiece(piece)

        for y in range (0,11):
            for x in range(0,11):
                if (isPiece(self.board[y][x])):
                    if (self.board[y][x].type == "serpent" or self.board[y][x].type == "grandempress"): 
                        #print (self.board[y][x].type,"at",self.board[y][x].y,self.board[y][x].x, "is a grandempress or serpent")

                        if (self.board[y][x].isPoisoned):
                            self.removePiece(self.board[y][x])

    def sumRow(self, y):
        numPieces = 0

        for x in range(0,11):
            if (isPiece(self.board[y][x])):
                numPieces += 1
        return numPieces

    def explode(self, joey):
        self.getAdjacent(joey)
        joey.isExploded = True
        for piece in joey.adjacent:
            if (piece.type == "joey"):
                piece.isExploded = True

            else:
                self.removePiece(piece)
        self.removePiece(joey)

    def checkJoey(self):
        numPieces = 0;
        whiteJoey = None
        blackJoey = None

        for y in range(0,11):
            for x in range(0,11):
                piece = self.board[y][x]
                if isPiece(piece):
                    if (piece.type == "princejoey"):
                        if (piece.colour == "white"):
                            whiteJoey = piece
                        elif (piece.colour == "black"):
                            blackJoey = piece

        if ((whiteJoey) and (blackJoey) and (whiteJoey.y == blackJoey.y)):
            numPieces = self.sumRow(whiteJoey.y)
            if (numPieces % 5 == 0):
                self.explode(whiteJoey)
                self.explode(blackJoey)
                if (blackJoey.isExploded):
                    self.removePiece(blackJoey)
                if (whiteJoey.isExploded):
                    self.removePiece(whiteJoey)
        else:
            if (whiteJoey):
                numPieces = self.sumRow(whiteJoey.y)
                if (numPieces % 5 == 0):
                    self.explode(whiteJoey)

            if (blackJoey):
                numPieces = self.sumRow(blackJoey.y)
                if (numPieces % 5 == 0):
                    self.explode(blackJoey)
    def promoteKing(self, king):
        y = king.y
        x = king.x
        colour = king.colour

        self.removePiece(king)

        if (colour == "white"):
            kingJetpack = KingJetPack(y, x, colour, "W")
        if (colour == "black"):
            kingJetpack = KingJetPack(y, x, colour, "w")

        self.board[y][x] = kingJetpack

    def checkKing(self):
        piece = self.board[5][5]
        if (isPiece(piece) and piece.type == "king"):
            self.promoteKing(piece)

    def afterEffects(self):
        transported = []

        self.checkKing()
        self.checkSerpents()
        # print ("\nafter serpents")
        # self.printState()

        self.checkCarts()
        # print ("\nafter golf carts")
        # self.printState()
        
        transported = self.checkTransporters()

        # print ("\nafter transporters")
        # self.printState()
        
        self.poisonRoundTwo(transported)
        # print ("\nafter serpents ROUND 2")
        # self.printState()

        self.checkJoey()
        # print ("\nafter joey")
        # self.printState()

    def checkTransporters(self):
        t1 = None
        t2 = None
        t3 = None
        t4 = None

        transported = []

        if (isPiece(self.board[3][1])):
            t1 = copy.deepcopy(self.board[3][1])

        if (isPiece(self.board[7][9])):
            t2 = copy.deepcopy(self.board[7][9])

        if (isPiece(self.board[7][1])):
            t3 = copy.deepcopy(self.board[7][1])

        if (isPiece(self.board[3][9])):
            t4 = copy.deepcopy(self.board[3][9])

        if (t1):
            self.board[7][9] = t1
            self.board[7][9].y = 7
            self.board[7][9].x = 9
            transported.append(self.board[7][9])
        else:
            self.board[7][9] = None

        if (t2):
            self.board[7][1] = t2
            self.board[7][1].y = 7
            self.board[7][1].x = 1
            transported.append(self.board[7][1])
        else:
            self.board[7][1] = None

        if (t3):
            self.board[3][9] = t3
            self.board[3][9].y = 3
            self.board[3][9].x = 9
            transported.append(self.board[3][9])
        else:
            self.board[3][9] = None

        if (t4):
            self.board[3][1] = t4
            self.board[3][1].y = 3
            self.board[3][1].x = 1
            transported.append(self.board[3][1])
        else:
            self.board[3][1] = None

        return transported

    def generateState(self, fileContents):
        self.initializeState()
        x = 0

        self.currentTurn = fileContents[0][0]
    
        for i in range(1,12):
            for j in range (0,11):
                symbol = fileContents[i][j]
                self.state[x][j] = symbol

                if (toPiece(symbol)):
                    newPiece = self.addPiece(symbol,x,j)
                    self.board[x][j] = newPiece
            x+=1

    def initializeState(self):
        self.state = [['.' for x in range(11)]for x in range(11)]
        self.board = [[None for x in range(11)]for x in range(11)]

    def printState(self):
        print ("  0 1 2 3 4 5 6 7 8 9 1")
        for y in range (0,11):
            if (y == 10):
                print ('1', end = " ")
            else:
                print(y, end=" ")
            for x in range (0,11):
                if (isPiece(self.board[y][x])):
                    print (self.board[y][x].letter, end=" ")
                else:
                    print(".", end=" ")
            print ("")

    def addPiece(self, letter, y, x):
        # White pieces
        if (letter == 'R'):
            newPiece = Rook(y, x, "white", letter)
        elif (letter == 'P'):
            newPiece = Pawn(y, x, "white", letter)
        elif (letter == 'N'):
            newPiece = Knight(y, x, "white", letter)
        elif (letter == 'Z'):
            newPiece = BeeKeeper(y, x, "white", letter)
        elif (letter == 'B'):
            newPiece = Bishop(y, x, "white", letter)
        elif (letter == 'O'):
            newPiece = OldWoman(y, x, "white", letter)
        elif (letter == 'K'):
            newPiece = King(y, x, "white", letter)
        elif (letter == 'X'):
            newPiece = GolfCart(y, x, "white", letter)
            self.whiteCart = newPiece
        elif (letter == 'C'):
            newPiece = Catapult(y, x, "white", letter)
        elif (letter == 'S'):
            newPiece = Serpent(y, x, "white", letter)
        elif (letter == 'J'):
            newPiece = PrinceJoey(y, x, "white", letter)
        elif (letter == 'G'):
            newPiece = Gorilla(y, x, "white", letter)
        elif (letter == 'H'):
            newPiece = TimeMachine(y, x, "white", letter)
        elif (letter == 'W'):
            newPiece = KingJetPack(y, x, "white", letter)
        elif (letter == 'E'):
            newPiece = GrandEmpress(y, x, "white", letter)

        # Black pieces
        elif (letter == 'r'):
            newPiece = Rook(y, x, "black", letter)
        elif (letter == 'p'):
            newPiece = Pawn(y, x, "black", letter)
        elif (letter == 'n'):
            newPiece = Knight(y, x, "black", letter)
        elif (letter == 'z'):
            newPiece = BeeKeeper(y, x, "black", letter)
        elif (letter == 'b'):
            newPiece = Bishop(y, x, "black", letter)
        elif (letter == 'o'):
            newPiece = OldWoman(y, x, "black", letter)
        elif (letter == 'k'):
            newPiece = King(y, x, "black", letter)
        elif (letter == 'x'):
            newPiece = GolfCart(y, x, "black", letter)
            self.blackCart = newPiece
        elif (letter == 'c'):
            newPiece = Catapult(y, x, "black", letter)
        elif (letter == 's'):
            newPiece = Serpent(y, x, "black", letter)
        elif (letter == 'j'):
            newPiece = PrinceJoey(y, x, "black", letter)
        elif (letter == 'g'):
            newPiece = Gorilla(y, x, "black", letter)
        elif (letter == 'h'):
            newPiece = TimeMachine(y, x, "black", letter)
        elif (letter == 'w'):
            newPiece = KingJetPack(y, x, "black", letter)
        elif (letter == 'e'):
            newPiece = GrandEmpress(y, x, "black", letter)

        if newPiece.colour == "white":
            self.whitePieces.append(newPiece)
        elif newPiece.colour == "black":
            self.blackPieces.append(newPiece)

        return newPiece
    #def movePieces(self):
     #   for y in self.state