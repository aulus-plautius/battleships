from lib.player import Player
from lib.players import Players
"""
Players object is initially has two player objects
objects save as an attribute
"""
def test_initially_has_two_player_objects():
    players = Players()
    assert isinstance(players.players[0], Player)
    assert isinstance(players.players[1], Player)

"""
Given a players object
Player game attributes can be accessed
"""
def test_player_game_attributes_are_accessible():
    players = Players()
    unplaced_ships = players.players[0].unplaced_ships
    assert len(unplaced_ships) == 5
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 3
    assert unplaced_ships[3].length == 4
    assert unplaced_ships[4].length == 5

"""
Given player 0 has one ship on the board
player 1 chooses a row and col which hits the ship
#fire returns True
"""
def test_hit_on_board_with_one_ship_returns_true():
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=3, col=2)
    assert players.check_if_hit_or_miss(player_number=1, row=3, col=2) == True

"""
If a player calls fire and hits
the row and column is saved into the player.hits attribute
"""
def test_hit_is_saved_in_attribute():
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=3, col=2)
    if players.check_if_hit_or_miss(player_number=1, row=3, col=2):
        pass
    assert players.players[1].hits == [(3,2)]

"""
If a player calls fire and misses
the row and column is saved into the player.misses attribute
"""
def test_miss_is_saved_in_attribute():
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=3, col=2)
    players.check_if_hit_or_miss(player_number=1, row=6, col=7)
    assert players.players[1].misses == [(6,7)]

"""
If player 1 sinks a ship of length 2
#check_sunk_ship returns true
"""
def test_player_sinks_ship_of_2():
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=3, col=2)
    players.check_if_hit_or_miss(player_number=1, row=3, col=2)
    players.check_if_hit_or_miss(player_number=1, row=4, col=2)
    assert players.check_if_shot_sinks_opponents_ship(player_number=1) == True
    assert players.players[1].ships_sunk[0].length == 2

"""
player 0 has a board of five ships
players 1 makes 5 shots and hits everytime
on the fifth shot player 1 sinks a boat of length 2
#check_ship_sunk return true
"""
def test_player_sinks_ship_of_2_after_5_shots():
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=2, col=2)
    players.players[0].place_ship(length=3, orientation="vertical", row=3, col=4)
    players.players[0].place_ship(length=3, orientation="vertical", row=4, col=6)
    players.players[0].place_ship(length=4, orientation="vertical", row=7, col=2)
    players.players[0].place_ship(length=5, orientation="vertical", row=3, col=9)
    players.check_if_hit_or_miss(player_number=1, row=2, col=2)
    players.check_if_hit_or_miss(player_number=1, row=3, col=9)
    players.check_if_hit_or_miss(player_number=1, row=4, col=9)
    players.check_if_hit_or_miss(player_number=1, row=7, col=2)
    players.check_if_hit_or_miss(player_number=1, row=3, col=2)
    assert players.check_if_shot_sinks_opponents_ship(player_number=1) == True
    assert len(players.players[1].hits) == 5
    assert len(players.players[1].ships_sunk) == 1
"""
player 0 has a board of five ships
players 1 makes 5 shots and hits everytime
on the 3rd shot sinks a boat of length 3
on the 5th shot sinks a boat of length 2
#check_ship_sunk return true
"""
def test_player_sinks_ship_of_3_then_2_after_5_shots():
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=2, col=2)
    players.players[0].place_ship(length=3, orientation="vertical", row=3, col=4)
    players.players[0].place_ship(length=3, orientation="vertical", row=4, col=6)
    players.players[0].place_ship(length=4, orientation="vertical", row=7, col=2)
    players.players[0].place_ship(length=5, orientation="vertical", row=3, col=9)
    players.check_if_hit_or_miss(player_number=1, row=3, col=4)
    players.check_if_shot_sinks_opponents_ship(player_number=1)
    players.check_if_hit_or_miss(player_number=1, row=4, col=4)
    players.check_if_shot_sinks_opponents_ship(player_number=1)
    players.check_if_hit_or_miss(player_number=1, row=5, col=4)
    players.check_if_shot_sinks_opponents_ship(player_number=1)
    players.check_if_hit_or_miss(player_number=1, row=2, col=2)
    players.check_if_shot_sinks_opponents_ship(player_number=1)
    players.check_if_hit_or_miss(player_number=1, row=3, col=2)
    assert players.check_if_shot_sinks_opponents_ship(player_number=1) == True
    assert players.players[1].ships_sunk[-1].length == 2
    assert players.players[1].ships_sunk[0].length == 3

"""
Given two names, #set_names
sets both player object name
"""
    
def test_set_names_sets_two_names():
    players = Players()
    players.set_names('joe', 'harriet')
    assert players.players == [
        Player(0, 'Joe'),
        Player(1, 'Harriet')
    ]
