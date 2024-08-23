from lib.game import Game
class Player(Game):
    def __init__(self, number, name = '') -> None:
        self.number = number
        self.name = name
        self.misses = []
        self.hits = []
        super().__init__(rows=10, cols=10)

    def __repr__(self) -> str:
        return f"Player({self.number}, {self.name})"
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__



    