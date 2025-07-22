from controllers.GameController import GameController
from models.Bot import Bot
from models.BotDifficulty import BotDifficulty
from models.GameStatus import GameStatus
from models.Player import Player
from models.PlayerType import PlayerType
from models.Symbol import Symbol
from services.GameService import GameService

if __name__ == '__main__':
    print("Welcome to the tictactoe game")

    gameService = GameService()
    gameController = GameController(gameService)

    dimension = 3
    players = [Player('Tapas',1,PlayerType.HUMAN,Symbol('X')),
               Bot('BOT',2,Symbol('O'),BotDifficulty.EASY)]
    winning_strategies = []

    game = gameController.create_game(dimension,players, winning_strategies)
    print(f'game created {game}')

    gameController.print_board(game)

    while game.game_status == GameStatus.IN_PROGRESS:
        gameController.make_move(game)
        gameController.print_board(game)
