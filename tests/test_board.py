from lib.player import Player
from lib.board import Board
from lib.players import Players

"""
If a player has placed no ships
#format_board creates an empty board
"""
def test_player_has_placed_no_ships_empty_board():
    player = Player(0)
    board = Board()
    assert board.format_board(player) == "\n".join(["    0 1 2 3 4 5 6 7 8 9  ",
                                                    "  ┌─────────────────────┐",
                                                    "0 │ · · · · · · · · · · │",
                                                    "1 │ · · · · · · · · · · │",
                                                    "2 │ · · · · · · · · · · │",
                                                    "3 │ · · · · · · · · · · │",
                                                    "4 │ · · · · · · · · · · │",
                                                    "5 │ · · · · · · · · · · │",
                                                    "6 │ · · · · · · · · · · │",
                                                    "7 │ · · · · · · · · · · │",
                                                    "8 │ · · · · · · · · · · │",
                                                    "9 │ · · · · · · · · · · │",
                                                    "  └─────────────────────┘"
                                                ])

"""
If a player has placed 5 ships
#format_board creates a board with five ships
"""
def test_player_has_placed_ships():
    player = Player(0)
    player.place_ship(length=2, orientation="vertical", row=2, col=2)
    player.place_ship(length=3, orientation="vertical", row=3, col=4)
    player.place_ship(length=3, orientation="vertical", row=4, col=6)
    player.place_ship(length=4, orientation="horizontal", row=8, col=2)
    player.place_ship(length=5, orientation="vertical", row=3, col=9)
    board = Board()
    assert board.format_board(player) == "\n".join(["    0 1 2 3 4 5 6 7 8 9  ",
                                                    "  ┌─────────────────────┐",
                                                    "0 │ · · · · · · · · · · │",
                                                    "1 │ · S · · · · · · · · │",
                                                    "2 │ · S · S · · · · S · │",
                                                    "3 │ · · · S · S · · S · │",
                                                    "4 │ · · · S · S · · S · │",
                                                    "5 │ · · · · · S · · S · │",
                                                    "6 │ · · · · · · · · S · │",
                                                    "7 │ · S S S S · · · · · │",
                                                    "8 │ · · · · · · · · · · │",
                                                    "9 │ · · · · · · · · · · │",
                                                    "  └─────────────────────┘"
                                                ])
    
"""
If a player has no hits or misses
#format_enemy_board creates an empty board
"""
def test_player_has_no_shots_enemy_empty_board():
    player = Player(0)
    board = Board()
    assert board.format_enemy_board(player) == "\n".join([  "    0 1 2 3 4 5 6 7 8 9  ",
                                                            "  ┌─────────────────────┐",
                                                            "0 │ · · · · · · · · · · │",
                                                            "1 │ · · · · · · · · · · │",
                                                            "2 │ · · · · · · · · · · │",
                                                            "3 │ · · · · · · · · · · │",
                                                            "4 │ · · · · · · · · · · │",
                                                            "5 │ · · · · · · · · · · │",
                                                            "6 │ · · · · · · · · · · │",
                                                            "7 │ · · · · · · · · · · │",
                                                            "8 │ · · · · · · · · · · │",
                                                            "9 │ · · · · · · · · · · │",
                                                            "  └─────────────────────┘"
                                                        ])
"""
If a player has one hit
#format_enemy_board creates a board with one hit and one miss
"""
def test_player_hits_enemy_board_shows_hit():
    board = Board()
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=3, col=2)
    players.check_if_hit_or_miss(player_number=1, row=3, col=2) == True
    assert board.format_enemy_board(players.players[1]) == "\n".join([  "    0 1 2 3 4 5 6 7 8 9  ",
                                                            "  ┌─────────────────────┐",
                                                            "0 │ · · · · · · · · · · │",
                                                            "1 │ · · · · · · · · · · │",
                                                            "2 │ · X · · · · · · · · │",
                                                            "3 │ · · · · · · · · · · │",
                                                            "4 │ · · · · · · · · · · │",
                                                            "5 │ · · · · · · · · · · │",
                                                            "6 │ · · · · · · · · · · │",
                                                            "7 │ · · · · · · · · · · │",
                                                            "8 │ · · · · · · · · · · │",
                                                            "9 │ · · · · · · · · · · │",
                                                            "  └─────────────────────┘"
                                                        ])
"""
If a player has one hit and one miss
#format_enemy_board creates a board with one hit and one miss
"""
def test_player_hits_enemy_board_and_misses_shows_hit_and_miss():
    board = Board()
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=3, col=2)
    players.check_if_hit_or_miss(player_number=1, row=3, col=2)
    players.check_if_hit_or_miss(player_number=1, row=10, col=10)
    assert board.format_enemy_board(players.players[1]) == "\n".join([  "    0 1 2 3 4 5 6 7 8 9  ",
                                                            "  ┌─────────────────────┐",
                                                            "0 │ · · · · · · · · · · │",
                                                            "1 │ · · · · · · · · · · │",
                                                            "2 │ · X · · · · · · · · │",
                                                            "3 │ · · · · · · · · · · │",
                                                            "4 │ · · · · · · · · · · │",
                                                            "5 │ · · · · · · · · · · │",
                                                            "6 │ · · · · · · · · · · │",
                                                            "7 │ · · · · · · · · · · │",
                                                            "8 │ · · · · · · · · · · │",
                                                            "9 │ · · · · · · · · · O │",
                                                            "  └─────────────────────┘"
                                                        ])
    
"""
A player sinks a ship
#format enemy board shows the hit "X" then sunk "#"
"""
def test_player_hits_and_sinks():
    board = Board()
    players = Players()
    players.players[0].place_ship(length=2, orientation="vertical", row=3, col=2)
    players.check_if_hit_or_miss(player_number=1, row=3, col=2)
    assert board.format_enemy_board(players.players[1]) == "\n".join([  "    0 1 2 3 4 5 6 7 8 9  ",
                                                            "  ┌─────────────────────┐",
                                                            "0 │ · · · · · · · · · · │",
                                                            "1 │ · · · · · · · · · · │",
                                                            "2 │ · X · · · · · · · · │",
                                                            "3 │ · · · · · · · · · · │",
                                                            "4 │ · · · · · · · · · · │",
                                                            "5 │ · · · · · · · · · · │",
                                                            "6 │ · · · · · · · · · · │",
                                                            "7 │ · · · · · · · · · · │",
                                                            "8 │ · · · · · · · · · · │",
                                                            "9 │ · · · · · · · · · · │",
                                                            "  └─────────────────────┘"
                                                        ])
    players.check_if_hit_or_miss(player_number=1, row=4, col=2)
    players.check_if_shot_sinks_opponents_ship(1)
    assert board.format_enemy_board(players.players[1]) == "\n".join([  "    0 1 2 3 4 5 6 7 8 9  ",
                                                                        "  ┌─────────────────────┐",
                                                                        "0 │ · · · · · · · · · · │",
                                                                        "1 │ · · · · · · · · · · │",
                                                                        "2 │ · # · · · · · · · · │",
                                                                        "3 │ · # · · · · · · · · │",
                                                                        "4 │ · · · · · · · · · · │",
                                                                        "5 │ · · · · · · · · · · │",
                                                                        "6 │ · · · · · · · · · · │",
                                                                        "7 │ · · · · · · · · · · │",
                                                                        "8 │ · · · · · · · · · · │",
                                                                        "9 │ · · · · · · · · · · │",
                                                                        "  └─────────────────────┘"
                                                                    ])

