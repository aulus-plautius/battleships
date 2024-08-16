from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.ships_placed = []
        self.ships_remaining = []
        self.ships_sunk = []
        self.rows = rows
        self.cols = cols
        self.unplaced_ships = [Ship(2),Ship(3),Ship(3),Ship(4),Ship(5)]


    def place_ship(self, length, orientation, row, col):
        ship_placement = ShipPlacement(
            length=length,
            orientation=orientation,
            row=row,
            col=col,
        )
        self.ships_placed.append(ship_placement)
        self.ships_remaining.append(ship_placement)
        self._remove_placed_ship(ship_placement)

    def _remove_placed_ship(self, ship_placement):
        for ship in self.unplaced_ships:
            if ship.length == ship_placement.length:
                self.unplaced_ships.remove(ship)
                break

    def check_ship_placement(self, length, orientation, row, col):
        ship_placement = ShipPlacement(length,orientation,row,col)
        return not (self._check_ship_overlaps(ship_placement) or 
            self._check_ship_out_of_bounds(ship_placement))


    def _check_ship_overlaps(self, ship_placement):
        for row, col in zip(ship_placement.ship_rows, ship_placement.ship_columns):
            if self.ship_at(row, col):
                return True
            
    def _check_ship_out_of_bounds(self, ship_placement):
        for row, col in zip(ship_placement.ship_rows, ship_placement.ship_columns):
            if row > 10 or row < 1 or col > 10 or col < 1:
                return True
            
    
    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
    
    def sunk_ship_at(self, row, col):
        for ship_placement in self.ships_sunk:
            if ship_placement.covers(row, col):
                return True
        return False
    
    
