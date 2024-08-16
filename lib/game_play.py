from lib.interaction_handler import InteractionHandler
from lib.board import Board
from lib.missile import Missile

class GamePlay(InteractionHandler):
    def __init__(self, io, players) -> None:
        self.players = players
        self.game_active = True
        self.winner = None
        self.io = io
        super().__init__(io=io)

    def play_round(self):
        for player in self.players.players:
            self.winner = player
            self._show(f"Player {player.number}, its your turn!")
            self._show("Enemy ships:")
            self._show(Board().format_enemy_board(player))
            missile = Missile(self.io, self.players)
            missile.fire(player)
            self.game_active = missile.game_active
            if not self.game_active:
                break
            self._show("Remaining enemy ships: {}".format(
                self._enemy_ships_remaining_message(player.number)))
            self._prompt("Press enter to finish.")
            print("\033c", end="")

    def _enemy_ships_remaining_message(self, player_number):
        opponent = self.players.players[abs(player_number-1)]
        opponent_ships = [str(ship.length) for ship in opponent.ships_remaining]
        return ", ".join(sorted(opponent_ships))