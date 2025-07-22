from models.CellStatus import CellStatus

class Player:
    def __init__(self,name,payer_id, player_type, symbol):
        self.name = name
        self.id = payer_id
        self.player_type = player_type
        self.symbol = symbol

    def decide_cell(self, board):
        while True:
            row = int(input('Enter row: '))
            column = int(input('Enter column: '))
            if  (0 <= row < board.dimension and 0 <= column < board.dimension and board.board[row][column].cell_status == CellStatus.EMPTY):
                break
            print('Invalid row/column or cell is not empty. Please try again...')
        return board.board[row][column]


