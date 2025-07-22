from models.CellStatus import CellStatus


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


    def print_board(self, game):
        game.board.printBoard()


    def make_move(self,game):
        current_player = game.players[game.next_player]
        print(f'Next turn is of: {current_player.name}')
        cell = current_player.decide_cell(game.board)
        cell.cell_status = CellStatus.FILLED
        cell.player = current_player
        game.next_player = (game.next_player+1) % len(game.players)

