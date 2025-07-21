
class GameController:
    def __init__(self,gameService):
        self.gameService = gameService


    def create_game(self,dimension,players, winning_strategies):
        return self.gameService.create_game(dimension, players, winning_strategies)

    def make_move(self):
        pass


