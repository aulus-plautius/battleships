from lib.interaction_handler import InteractionHandler
from lib.format_board import FormatBoard
from lib.generate_image import GenerateImage
from lib.take_aim import TakeAim
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
            row, col = TakeAim(self.io).get_position(player)
            if self.players.check_if_hit_or_miss(player.number, row, col):
                self._clear_terminal()
                if self.players.check_if_shot_sinks_opponents_ship(player.number):
                    self._sink_message(player)
                else:
                    self._hit_message(player)
            else:
                self._miss_message(player)

    def _sink_message(self, player):
        ship_num = player.ships_sunk[-1].length
        self._player_turn_message(player)
        self._show(GenerateImage().sink)
        sleep(1)
        self._clear_terminal()
        self._show(f"Ship Sunk! You sunk a {ship_num}!")
        self._show("Enemy ships:")
        self._show(FormatBoard().enemy_ships(player))
        if self._check_win():
            self.game_active = False
            self.active_shot = False

    def _hit_message(self, player):
        self._player_turn_message(player)
        self._show(GenerateImage().hit)
        sleep(1)
        self._clear_terminal()
        # print("\033c", end="")
        self._player_turn_message(player)
        self._show(FormatBoard().enemy_ships(player))

    def _miss_message(self, player):
        self._clear_terminal()
        # print("\033c", end="")
        self._player_turn_message(player)
        self._show(GenerateImage().miss)
        sleep(1)
        self._clear_terminal()
        # print("\033c", end="")
        self._player_turn_over_message(player)
        self._show(FormatBoard().enemy_ships(player))
        self.active_shot = False

    def _player_turn_over_message(self, player):
        self._show(f"{player.name}, your turn is over!")
        self._show("Enemy ships:")

    def _player_turn_message(self, player):
        self._show(f"{player.name}, its your turn!")
        self._show("Enemy ships:")

    def _check_win(self):
        return (len(self.players.players[0].ships_remaining) == 0 or
                len(self.players.players[1].ships_remaining) == 0)