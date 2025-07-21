import random
from models.Board import Board
from models.GameStatus import GameStatus

class Game:
    def __init__(self,dimension,players,winning_strategies):
        self.dimension = dimension
        self.players = players
        self.winning_strategies = winning_strategies
        self.board = Board(self.dimension)
        self.game_status = GameStatus.IN_PROGRESS
        self.winner = None
        self.next_player = random.randint(0,self.dimension-1)

    @staticmethod
    def gameBuilder():
        from helper.GameBuilder import GameBuilder
        return GameBuilder()
