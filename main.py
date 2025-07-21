from controllers.GameController import GameController
from models.Bot import Bot
from models.BotDifficulty import BotDifficulty
from models.Player import Player
from models.PlayerType import PlayerType
from services.GameService import GameService

if __name__ == '__main__':
    print("Welcome to the tictactoe game")

    gameService = GameService()
    gameController = GameController(gameService)

    dimension = 3
    players = [Player('Tapas',1,PlayerType.HUMAN,'X'),
               Bot('BOT',2,'O',BotDifficulty.EASY)]
    winning_strategies = []

    game = gameController.create_game(dimension,players, winning_strategies)
    print(f'game created {game}')
