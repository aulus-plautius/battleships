from lib.interaction_handler import InteractionHandler

class Aim(InteractionHandler):
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
        while True:
            row = self._prompt("Row:")
            if row.isdigit() and -1 < int(row) < 10:
                break
            self._show("Invalid row, try again!")
        return int(row) + 1

    def _prompt_for_shot_column(self):
        while True:
            column = self._prompt("Column:")
            if column.isdigit() and -1 < int(column) < 10:
                break
            self._show("Invalid column, try again!")
        return int(column) + 1