from lib.player import Player
# from lib.game import Game
"""
Initialises with a player number
"""
def test_initially_bot_attr_is_set_to_false():
    player = Player(0)
    assert player.number == 0


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

