
class GameController:
    def __init__(self,gameService):
        self.gameService = gameService


    def create_game(self,dimension,players, winning_strategies):
        return self.gameService.create_game(dimension, players, winning_strategies)

    def print_board(self, game):
        self.gameService.print_board(game)

    def validate_move(self,game,row,column):
        return self.gameService.validate_move(game,row,column)

    def make_move(self, game):
        self.gameService.make_move(game)

