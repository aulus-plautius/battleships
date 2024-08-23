from lib.interaction_handler import InteractionHandler
from lib.game_setup import GameSetUp
from lib.game_play import GamePlay
from lib.players import Players
class UserInterface(InteractionHandler):
    def __init__(self, io):
        self.io = io
        self.players = Players()
        self.game_active = True

    def run(self):
        self._show("Welcome to the game!")
        name1 = self._prompt("Please enter player 1's name:")
        name2 = self._prompt("Please enter player 2's name:")
        self.players.set_names(name1, name2)
        self._clear_terminal()
        GameSetUp(self.io, self.players).set_up_ships()
        gameplay = GamePlay(self.io, self.players)
        while self.game_active:
            gameplay.play_round()
            self.game_active = gameplay.game_active
            self.winner = gameplay.winner
        self._show("Game Over!")
        self._show(f"{self.winner.name} wins!")




    

