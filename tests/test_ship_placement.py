from lib.ship_placement import ShipPlacement

"""
Initialises with a length, orientation, row, and col
"""
def test_initialises_with_a_length_orientation_row_and_col():
    ship_placement = ShipPlacement(
        length=5, orientation="vertical", row=3, col=2)
    assert ship_placement.length == 5
    assert ship_placement.orientation == "vertical"
    assert ship_placement.row == 3
    assert ship_placement.col == 2


"""
Checks if vertical ships cover a given row and col
"""
def test_checks_if_vertical_ships_cover_a_given_row_and_col():
    ship_placement = ShipPlacement(
        length=5, orientation="vertical", row=3, col=2)
    assert ship_placement.covers(3, 2)
    assert ship_placement.covers(4, 2)
    assert ship_placement.covers(5, 2)
    assert ship_placement.covers(6, 2)
    assert ship_placement.covers(7, 2)
    assert not ship_placement.covers(2, 2)
    assert not ship_placement.covers(8, 2)
    assert not ship_placement.covers(3, 1)
    assert not ship_placement.covers(3, 3)


"""
Checks if horizontal ships cover a given row and col
"""
def test_checks_if_horizontal_ships_cover_a_given_row_and_col():
    ship_placement = ShipPlacement(
        length=5, orientation="horizontal", row=3, col=2)
    assert ship_placement.covers(3, 2)
    assert ship_placement.covers(3, 3)
    assert ship_placement.covers(3, 4)
    assert ship_placement.covers(3, 5)
    assert ship_placement.covers(3, 6)
    assert not ship_placement.covers(3, 1)
    assert not ship_placement.covers(3, 7)
    assert not ship_placement.covers(2, 2)
    assert not ship_placement.covers(4, 2)


"""
Has a friendly string representation
"""
def test_has_a_friendly_string_representation():
    ship_placement = ShipPlacement(
        length=5, orientation="horizontal", row=3, col=2)
    assert str(
        ship_placement) == "ShipPlacement(length=5, orientation=horizontal, row=3, col=2)"
    
"""
Given a ship at row 2 column 2 and vertical of length 2
Object has rows and column attribute
"""
def test_given_a_vert_ship_of_length_2_at_row2_column_2_returns_rows_and_cols():
    ship_placement = ShipPlacement(
        length=2, orientation="vertical", row=2, col=2)
    assert ship_placement.ship_rows == [2,3]
    assert ship_placement.ship_columns == [2,2]

"""
Given a ship at row 4 column 6 and horizontal of length 4
Object has rows and column attribute
"""
def test_given_a_hori_ship_of_length_4_at_row4_column6_returns_rows_and_cols():
    ship_placement = ShipPlacement(
        length=4, orientation="horizontal", row=4, col=6)
    assert ship_placement.ship_rows == [4,4,4,4]
    assert ship_placement.ship_columns == [6,7,8,9]
