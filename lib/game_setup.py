from lib.interaction_handler import InteractionHandler
from lib.format_board import FormatBoard
class GameSetUp(InteractionHandler):
    def __init__(self, io, players) -> None:
        self.players = players
        super().__init__(io=io)

    def set_up_ships(self):
        for player in self.players.players:
            self._show(f"{player.name}, set up your ships first.")
            self._show("This is your board:")
            self._show(FormatBoard().player_ships(player))
            while len(player.unplaced_ships) > 0:
                self._show("You have these ships remaining: {}".format(
                    self._ships_unplaced_message(player)))
                self._prompt_for_ship_placement(player)
                self._clear_terminal()
                self._show("This is your board now:")
                self._show(FormatBoard().player_ships(player))
            self._prompt("Press enter to finish.")
            self._clear_terminal()

    def _ships_unplaced_message(self, player):
        ship_lengths = [str(ship.length) for ship in player.unplaced_ships]
        return ", ".join(ship_lengths)
    
    def _prompt_for_ship_placement(self, player):
        while True:
            length = int(self._prompt_for_length(player))
            orientation = {"v": "vertical", "h": "horizontal"}[self._prompt_for_orientation()]
            while True:
                row = int(self._prompt_for_row())
                col = int(self._prompt_for_column())
                if player.check_ship_placement(length,orientation,row,col):
                    self._show("OK.")
                    player.place_ship(length,orientation,row,col)
                    break
                else:
                    self._show("Invalid placement, try again!")
            break

    def _prompt_for_length(self, player):
        # while True:
        #     ship_length = self._prompt("Which do you wish to place?")
        #     if ship_length in [str(ship.length) for ship in player.unplaced_ships]:
        #         break
        #     else:
        #         self._show("Invalid ship, try again!")
        # return ship_length
        ship_length = player.unplaced_ships[0].length
        self._show(f"Place your ship: {ship_length}")
        return ship_length

    def _prompt_for_orientation(self):
        while True:
            ship_orientation = self._prompt("Vertical or horizontal? [vh]")
            if ship_orientation in ["v","h"]:
                break
            self._show("Invalid orientation, try again!")
        return ship_orientation
    
    def _prompt_for_row(self):
        row_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
        while True:
            ship_row = self._prompt("Which row?")
            if ship_row.lower() in row_dict.keys():
                break
            self._show("Invalid row, try again!")
        return row_dict[ship_row.lower()]

    def _prompt_for_column(self):
        while True:
            ship_column = self._prompt("Which column?")
            if ship_column.isdigit():
                break
            self._show("Invalid column, try again!")
        return int(ship_column) + 1