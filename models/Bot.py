from models.Player import Player
from models.PlayerType import PlayerType


class Bot(Player):
    def __init__(self,name, player_id,symbol,difficulty_level ):
        super().__init__(name, player_id, PlayerType.BOT, symbol)
        self.difficulty_level = difficulty_level

