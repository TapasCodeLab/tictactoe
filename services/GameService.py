

class GameService:
    def __init__(self):
        pass

    def create_game(self,dimension,players, winning_strategies):
        from models.Game import Game
        return (Game.gameBuilder()
                     .set_dimension(dimension)
                     .set_players(players)
                     .set_winning_strategies(winning_strategies)
                     .build())


