from lib.game import Game
class Player(Game):
    def __init__(self, number) -> None:
        self.number = number
        self.misses = []
        self.hits = []
        super().__init__(rows=10, cols=10)



    