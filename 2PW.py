#!/usr/bin/env python

#Spencer Walker
#0715530
#March 15th 2015
#2PW Chess Variant AI

from __future__ import print_function

import fileinput
import sys
import pdb
import copy;

from board import *
from sys import stdin
import logging
import Colorer
import random

class TPW:

    whiteTurns = 0
    blackTurns = 0
    stateCount = 0
    line1 = ""
    line2 = ""
    line3 = ""

    def __init__(self, state, root=False):
        self.state = state
        # The current representation of the board
        self.currentTurn = ""
        self.path = ""

        self.initializeBoard()
        # self.printBoard();

        self.parseState()
        self.generateStates()

        if root:
            self.visited = []
    
    def printFile(self,board):
        f = open("board."+str(self.stateCount).zfill(3), 'w')
        if (self.currentTurn == 'W'):
            f.write('B\n')
        elif (self.currentTurn == 'B'):
            f.write('W\n')

        for i in range(0,11):
            for j in range(0,11):
                f.write(board[i][j])
            f.write('\n')
        f.write('0\n')
        f.write('0\n')
        f.write('0\n')
        f.close()

maximizer = ""

def lookAhead(board):
    highestMin = 0

    for y in range(0,11):
        for x in range (0,11):
            piece = board.board[y][x]
            if (isPiece(piece) == False):
                continue

            if (board.currentTurn == "B"):
                if piece.colour == "white":
                    continue
            elif (board.currentTurn == "W"):
                if piece.colour == "black":
                    continue

            for move in piece.legalMoves:
                newBoard = copy.deepcopy(board)

                newBoard.playMove(newBoard.board[y][x], move)
                newBoard.afterEffects()

                nextBoards.append(newBoard)

    for board in nextBoards:
        board.calculatePieceScores()

    #Sort for lowest score
    if (board.currentTurn == "B"):
        nextBoards.sort(key=lambda x: x.whiteScore, reverse=False)
        return nextBoards[0].whiteScore

    if (board.currentTurn == "W"):
        nextBoards.sort(key=lambda x: x.blackScore, reverse=False)
        return nextBoards[0].blackScore

def determineBestMove(boards):
    # bestPlay = ()

    # for board in boards:
    #     bestPlay = getMax(board, 2)
    #     print bestPlay
    #     sys.exit()


    nextBoard = []
    highestMin = 0;
    location = 0

    for i, board in enumerate(boards):
        #board.calculatePieceScores()
        nextBoard = board.toMinMaxFormat()

        newBoard = Board(nextBoard)
        newBoard.movePieces()
        newMin = lookAhead(newBoard)
        print("newMin = ", newMin)
        if (newMin > highestMin):
            highestMin = newMin
            location = i
        
    print("highest min: ",highestMin)
    sys.exit()

    return boards[location]

    #Sort for highest score
    # if (board.currentTurn == "W"):
    #     boards.sort(key=lambda x: x.whiteScore, reverse=True)
    # if (board.currentTurn == "B"):
    #     boards.sort(key=lambda x: x.blackScore, reverse=True)

    # return boards[0]


def getNextBoards(curBoard):
    curBoard.movePieces()
    newBoards = []

    for y in range(0,11):                  #Generate new board for all legal moves
        for x in range (0,11):
            piece = curBoard.board[y][x]
            if (isPiece(piece) == False):
                continue

            if (curBoard.currentTurn == "B"):
                if piece.colour == "white":
                    continue
            elif (curBoard.currentTurn == "W"):
                if piece.colour == "black":
                    continue

            for move in piece.legalMoves:
                newBoard = copy.deepcopy(curBoard)
                newBoard.playMove(newBoard.board[y][x], move)
                newBoard.afterEffects()
                #newBoard.calculateScores()              #Determine score for each board

                newBoards.append(newBoard)
    return newBoards

def getMin(cBoard, depth):
    print ("depth = ", depth)
    #currentBoard.printState()
    if (depth == 0):
        cBoard.whiteScore = random.randrange(1,100)
        #currentBoard.calculateScore()
        if (maximizer == "B"):
            return ((cBoard.blackScore, None))
        elif (maximizer == "W"):
            return ((cBoard.whiteScore, None))
        else:
            return cBoard.whiteScore

    #maybe comment this out for testing
    if maximizer == "W":
        cBoard.curentTurn = "B"
    elif maximizer == "B":
        cBoard.currentTurn = "W"

    worstScore = 1000000
    #worstBoard = copy.deepcopy(currentBoard)
    print("moving pieces for ", cBoard.currentTurn)
    newBoardz = getNextBoards(copy.deepcopy(cBoard))
    for nBoard in newBoardz:
        score = getMax(copy.deepcopy(nBoard), depth-1)

        if (score[0] < worstScore):
            worstScore = score[0]
            worstBoard = copy.deepcopy(nBoard)

    worstBoard.printState()
    return ((worstScore, copy.deepcopy(worstBoard)))

def getMax(currentBoard, depth):
    print("depth = ", depth)
    #currentBoard.printState()
    if (depth == 0):
        currentBoard.whiteScore = random.randrange(1,100)
        if (maximizer == "B"):
            return ((currentBoard.blackScore, None))
        elif (maximizer == "W"):
            return ((currentBoard.whiteScore, None))
        else:
            return currentBoard.whiteScore

    currentBoard.currentTurn = maximizer

    bestScore = -1000000
    newBoards = getNextBoards(copy.deepcopy(currentBoard))
    for xBoard in newBoards:
        score = getMin(copy.deepcopy(xBoard), depth-1)

        if (score[0] > bestScore):
            bestScore = score[0]
            bestBoard = copy.deepcopy(xBoard)
    bestBoard.printState()
    return ((bestScore, copy.deepcopy(bestBoard)))

if __name__ == "__main__":

    #fileContents = ""
    fileContents = []
    legalMoves = []
    nextBoards = []
    hScore = 0
    bestBoard = None
    firstMove = False

    for line in fileinput.input(None):
        fileContents.append(line)

    board = Board(fileContents)
    maximizer = board.currentTurn

    tester = getMax(board, 3)
    tester[1].printState()
    sys.exit()

    #determineBestMove(nextBoards)    #will prbably need to move this to the ELSE

    if (board.checkFirstMove() == True):                #Hardcoded first move
        chosenBoard = board

        if (board.currentTurn == "W"):
            board.movePiece(board.board[1][5],(2,5))    #Move Joey up one space
        elif (board.currentTurn == "B"):
            board.movePiece(board.board[9][5],(8,5))

    else:
        if (board.currentTurn == "W"):
            nextBoards.sort(key=lambda x: x.whiteScore - x.blackScore, reverse=True)
            chosenBoard = nextBoards[0]

        if (board.currentTurn == "B"):
            nextBoards.sort(key=lambda x: x.blackScore - x.whiteScore, reverse=True)
            chosenBoard = nextBoards[0]

    chosenBoard.toFileFormat()
