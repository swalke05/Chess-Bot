from piece import *;
class TimeMachine(Piece):
    def __init__(self, y, x, colour, letter):
        Piece.__init__(self,y, x, colour, letter)
        self.type = "timemachine"
        self.isBiological = False
        self.score = 80