from models.Game import Game

class GameBuilder:
    def __init__(self):
        self.dimension = None
        self.players = None
        self.winning_strategies = None

    def set_dimension(self,dimension):
        self.dimension = dimension
        return self

    def set_players(self,players):
        self.players = players
        return self

    def set_winning_strategies(self,winning_strategies):
        self.winning_strategies = winning_strategies
        return self

    def validate(self):
        if self.dimension<=2:
            raise Exception
        if self.dimension != len(self.players) + 1:
            raise Exception
        if self.winning_strategies is None:
            raise Exception
        return self

    def build(self):
        self.validate()
        return Game(self.dimension,self.players,self.winning_strategies)
