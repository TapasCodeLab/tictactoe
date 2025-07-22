from helper.strategy.botStrategy.BotPlayingStrategy import BotPlayingStrategy
from models.CellStatus import CellStatus


class MediumPlayingStrategy(BotPlayingStrategy):

    def decide_cell(self, board):
        for row in board.board:
            for cell in row:
                if cell.cell_status == CellStatus.EMPTY:
                    return cell