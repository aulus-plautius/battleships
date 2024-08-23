from lib.interaction_handler import InteractionHandler

class TakeAim(InteractionHandler):
    def __init__(self, io) -> None:
        super().__init__(io)

    def get_position(self, player):
        while True:
            row = self._prompt_for_shot_row()
            col = self._prompt_for_shot_column()
            if (row, col) in player.misses or (row, col) in player.hits:
                self._show("Already shot here, try again!")
            else:
                break
        return row, col

    def _prompt_for_shot_row(self):
        row_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
        while True:
            ship_row = self._prompt("Row:")
            if ship_row.lower() in row_dict.keys():
                break
            self._show("Invalid row, try again!")
        return row_dict[ship_row.lower()]

    def _prompt_for_shot_column(self):
        while True:
            column = self._prompt("Column:")
            if column.isdigit() and -1 < int(column) < 10:
                break
            self._show("Invalid column, try again!")
        return int(column) + 1