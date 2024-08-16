from lib.interaction_handler import InteractionHandler
from lib.game_setup import GameSetUp
from lib.game_play import GamePlay
class UserInterface(InteractionHandler):
    def __init__(self, io, players):
        self.io = io
        self.players = players
        self.game_active = True

    def run(self):
        self._show("Welcome to the game!")
        GameSetUp(self.io, self.players).set_up_ships()
        gameplay = GamePlay(self.io, self.players)
        while self.game_active:
            gameplay.play_round()
            self.game_active = gameplay.game_active
            self.winner = gameplay.winner
        self._show("Game Over!")
        self._show(f"Player {self.winner.number} Wins!")




    

