from lib.game import Game
from unittest.mock import Mock
from lib.ship_placement import ShipPlacement
"""
Initialises with a length and width of 10
"""
def test_initialises_with_a_length_and_width_of_10():
    game = Game()
    assert game.rows == 10
    assert game.cols == 10


"""
Initialises with five ships of length 2, 3, 3, 4, 5
"""
def test_initialises_with_five_ships_of_right_length():
    game = Game()
    unplaced_ships = game.unplaced_ships
    assert len(unplaced_ships) == 5
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 3
    assert unplaced_ships[3].length == 4
    assert unplaced_ships[4].length == 5

"""
Initialises with a totally empty board
"""
def test_initialises_with_a_totally_empty_board():
    game = Game()
    for row in range(1, 11):
        for col in range(1, 11):
            assert not game.ship_at(row, col)

"""
When we place a ship
Then its place on the board is marked out
"""
def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():
    game = Game()
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert game.ship_at(3, 2)
    assert game.ship_at(4, 2)
    assert not game.ship_at(3, 3)
    assert not game.ship_at(4, 3)
    assert not game.ship_at(3, 1)
    assert not game.ship_at(4, 1)

"""
When a ship has been sunk
It is marked out
"""
def test_when_a_ship_has_been_sunk_it_is_marked_out():
    ship_placement = Mock()
    ship_placement.length = 2
    ship_placement.orientation = "vertical"
    ship_placement.row = 2
    ship_placement.col = 1
    game = Game()
    game.ships_sunk.append(ShipPlacement(2,"vertical",2,1))
    assert game.sunk_ship_at(2,1)
    assert game.sunk_ship_at(3,1)


"""
When we place 2 ships
Then both their places on the board are marked out
"""
def test_when_we_place_2_ships_then_their_places_on_the_board_are_marked_out():
    game = Game()
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert game.ship_at(3, 2)
    assert game.ship_at(4, 2)
    assert not game.ship_at(3, 3)
    assert not game.ship_at(4, 3)
    assert not game.ship_at(3, 1)
    assert not game.ship_at(4, 1)
    game.place_ship(length=3, orientation="horizontal", row=7, col=3)
    assert game.ship_at(7, 3)
    assert game.ship_at(7, 4)
    assert game.ship_at(7, 5)

"""
When we place two ships at the same coordinate
#check_ship_placement returns false
"""
def test_when_we_place_2_ships_at_the_same_coordinates_place_ship_returns_false():
    game = Game()
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert not game.check_ship_placement(length=3, orientation="vertical", row=3, col=2)

"""
When we place two ships but second coordinate is on a ship
#check_ship_placement returns false
"""
def test_when_we_place_2_ships_and_2nd_coordinate_is_placed_on_ship_returns_false():
    game = Game()
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert not game.check_ship_placement(length=3, orientation="vertical", row=4, col=2)

"""
When we place two ships but the second ship overlaps another ship
#check_ship_placement returns false
"""
def test_when_we_place_2_ships_and_2nd_ship_is_placed_on_ship_returns_false():
    game = Game()
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert not game.check_ship_placement(length=3, orientation="horiztonal", row=4, col=1)

"""
When we place a ship at a row that is out of bounds
#check_ship_placement returns false
"""
def test_when_we_place_a_ship_at_a_row_out_of_bounds_return_false():
    game = Game()
    assert not game.check_ship_placement(length=2, orientation="vertical", row=11, col=2)
    assert not game.check_ship_placement(length=2, orientation="vertical", row=0, col=2)
    

"""
When we place a ship at a column that is out of bounds
#check_ship_placement returns false
"""
def test_when_we_place_a_ship_at_a_row_out_of_bounds_return_false():
    game = Game()
    assert not game.check_ship_placement(length=2, orientation="vertical", row=2, col=0)
    assert not game.check_ship_placement(length=2, orientation="vertical", row=2, col=11)

"""
When we place a ship and part of it is out of bounds
#check_ship_placement returns false
"""
def test_when_we_place_a_ship_and_part_is_out_of_bounds_return_false():
    game = Game()
    assert not game.check_ship_placement(length=4, orientation="horiztonal", row=2, col=8)

"""
When a ship of length 3 is placed it is removed from the unplaced attribute
"""
def test_when_ship_length_3_is_placed_it_is_removed_from_unplaced():
    game = Game()
    game.place_ship(length=3, orientation="vertical", row=2, col=5)
    unplaced_ships = game.unplaced_ships
    assert len(unplaced_ships) == 4
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 4
    assert unplaced_ships[3].length == 5