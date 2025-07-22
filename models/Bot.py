from helper.BotFactory import BotFactory
from models.Player import Player
from models.PlayerType import PlayerType
from models.CellStatus import CellStatus

class Bot(Player):
    def __init__(self,name, player_id,symbol,difficulty_level ):
        super().__init__(name, player_id, PlayerType.BOT, symbol)
        self.difficulty_level = difficulty_level
        self.bot_strategy = BotFactory.getBotStrategy(difficulty_level)


    def decide_cell(self, board):
        return self.bot_strategy.decide_cell(board)

