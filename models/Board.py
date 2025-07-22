from models.Cell import Cell


class Board:
    def __init__(self, dimension):
        self.dimension = dimension
        self.board = [[Cell(row,col) for col in range(self.dimension)] for row in range(self.dimension)]



    def printBoard(self):
        for row in self.board:
            for cell in row:
                cell.printCell()
            print('|')
