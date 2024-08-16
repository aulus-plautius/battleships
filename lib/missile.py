from lib.interaction_handler import InteractionHandler
from lib.board import Board
from lib.image import Image
from lib.aim import Aim
from time import sleep

class Missile(InteractionHandler):
    def __init__(self, io, players) -> None:
        self.players = players
        self.active_shot = True
        self.game_active = True
        self.io = io
        super().__init__(io=io)

    def fire(self, player):
        while self.active_shot:
            self._show("Take a shot.")
            row, col = Aim(self.io).get_position(player)
            if self.players.check_if_hit_or_miss(player.number, row, col):
                print("\033c", end="")
                if self.players.check_if_shot_sinks_opponents_ship(player.number):
                    self._sink_message(player)
                else:
                    self._hit_message(player)
            else:
                self._miss_message(player)

    def _sink_message(self, player):
        ship_num = player.ships_sunk[-1].length
        self._show(f"Player {player.number}, its your turn!")
        self._show("Enemy ships:")
        self._show(Image().sink)
        sleep(1)
        print("\033c", end="")
        self._show(f"Ship Sunk! You sunk a {ship_num}!")
        self._show("Enemy ships:")
        self._show(Board().format_enemy_board(player))
        if (len(self.players.players[0].ships_remaining) == 0 or
            len(self.players.players[1].ships_remaining) == 0):
            self.game_active = False
            self.active_shot = False

    def _hit_message(self, player):
        self._show(f"Player {player.number}, its your turn!")
        self._show("Enemy ships:")
        self._show(Image().hit)
        sleep(1)
        print("\033c", end="")
        self._show(f"Player {player.number}, its your turn!")
        self._show("Enemy ships:")
        self._show(Board().format_enemy_board(player))

    def _miss_message(self, player):
        print("\033c", end="")
        self._show(f"Player {player.number}, its your turn!")
        self._show("Enemy ships:")
        self._show(Image().miss)
        sleep(1)
        print("\033c", end="")
        self._show(f"Player {player.number}, your turn is over!")
        self._show("Enemy ships:")
        self._show(Board().format_enemy_board(player))
        self.active_shot = False