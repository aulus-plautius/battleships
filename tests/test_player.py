from lib.player import Player
# from lib.game import Game
"""
Initialises with a player number
"""
def test_object_constructs_with_name_and_number():
    player = Player(0, 'name')
    assert player.number == 0
    assert player.name == 'name'


"""
Player object inherits game object
"""
def test_initially_game_object_is_saved_as_attr():
    player = Player(0)
    unplaced_ships = player.unplaced_ships
    assert len(unplaced_ships) == 5
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 3
    assert unplaced_ships[3].length == 4
    assert unplaced_ships[4].length == 5

"""
Hits and misses are initialised
"""
def test_initialises_with_hit_and_misses():
    player = Player(0)
    assert player.misses == []
    assert player.hits == []

"""
Player has formatted string
"""
def test_player_object_has_formatted_string():
    player = Player(0, 'name')
    assert str(player) == "Player(0, name)"

def test_two_objects_are_equal():
    player1 = Player(0, 'name')
    player2 = Player(0, 'name')
    assert player1 == player2
9
0