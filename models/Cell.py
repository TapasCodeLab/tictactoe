from models.CellStatus import CellStatus

class Cell:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.cell_status = CellStatus.EMPTY
        self.player = None


    def printCell(self):
        if self.cell_status == CellStatus.EMPTY:
            print('|-', end='')
        elif self.cell_status == CellStatus.FILLED:
            print(f'|{self.player.symbol.symbol}',end='')
        else:
            print('|B',end='')
