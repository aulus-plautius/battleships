import unittest

from lib.user_interface import UserInterface
from lib.players import Players
from lib.board import Board
from lib.ship import Ship
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock

from unittest.mock import Mock



class TestUserInterface(unittest.TestCase):
    def test_full_game_of_1_ship(self):
        io = TerminalInterfaceHelperMock()
        players = Players()
        players.players[0].unplaced_ships = [Ship(2)]
        players.players[1].unplaced_ships = [Ship(2)]
        interface = UserInterface(io, players)
        io.expect_print("Welcome to the game!")
        io.expect_print("Player 0, set up your ships first.")
        io.expect_print("This is your board:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
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
                                ]))
        io.expect_print("You have these ships remaining: 2")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("2")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "0 │ · · · · · · · · · · │",
                                    "1 │ · · · · · · · · · · │",
                                    "2 │ · S · · · · · · · · │",
                                    "3 │ · S · · · · · · · · │",
                                    "4 │ · · · · · · · · · · │",
                                    "5 │ · · · · · · · · · · │",
                                    "6 │ · · · · · · · · · · │",
                                    "7 │ · · · · · · · · · · │",
                                    "8 │ · · · · · · · · · · │",
                                    "9 │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Press enter to finish.")
        io.provide("")
# player 1 sets up their board -------------------------------------------------
        io.expect_print("Player 1, set up your ships first.")
        io.expect_print("This is your board:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
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
                                ]))
        io.expect_print("You have these ships remaining: 2")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("6")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "0 │ · · · · · · · · · · │",
                                    "1 │ · · · · · · · · · · │",
                                    "2 │ · · · · · · · · · · │",
                                    "3 │ · · · · · · · · · · │",
                                    "4 │ · · · · · · · · · · │",
                                    "5 │ · · · · · · S S · · │",
                                    "6 │ · · · · · · · · · · │",
                                    "7 │ · · · · · · · · · · │",
                                    "8 │ · · · · · · · · · · │",
                                    "9 │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Press enter to finish.")
        io.provide("")
# game starts ------------------------------------------------------------------
        io.expect_print("Player 0, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
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
                                ]))
        io.expect_print("Take a shot.")
        io.expect_print("Row:")
        io.provide("2")
        io.expect_print("Column:")
        io.provide("6")
        io.expect_print("Player 0, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "0 |                     |",
                                    "1 │       .-- .         │",
                                    "2 │     .(     )        │",
                                    "3 │   (       ))     _  │",
                                    "4 │  _ `- __.'    . ` ) │",
                                    "5 │  __ .  MISS! :(    )│",
                                    "6 │(     '`. .  `(     )│",
                                    "7 │(       ) )    ` _.' │",
                                    "8 │ `_.:'-'             │",
                                    "9 │~~~~~~~~~~~~~~~~~~~~~│",
                                    "  └─────────────────────┘"]))
        io.expect_print("Player 0, your turn is over!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "0 │ · · · · · · · · · · │",
                                    "1 │ · · · · · · · · · · │",
                                    "2 │ · · · · · · O · · · │",
                                    "3 │ · · · · · · · · · · │",
                                    "4 │ · · · · · · · · · · │",
                                    "5 │ · · · · · · · · · · │",
                                    "6 │ · · · · · · · · · · │",
                                    "7 │ · · · · · · · · · · │",
                                    "8 │ · · · · · · · · · · │",
                                    "9 │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Remaining enemy ships: 2")
        io.expect_print("Press enter to finish.")
        io.provide("")
        io.expect_print("Player 1, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
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
                                ]))
        io.expect_print("Take a shot.")
        io.expect_print("Row:")
        io.provide("2")
        io.expect_print("Column:")
        io.provide("1")
        io.expect_print("Player 1, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( [r"    0 1 2 3 4 5 6 7 8 9  ",
                                    r"  ┌─────────────────────┐",
                                    r"0 │  _.-^^---....,,--_  │",
                                    r"1 │_-                 -_│",
                                    r"2 │<        HIT!      >)│",
                                    r"3 │\.                 / │",
                                    r"4 │  ```--. . , ; .--'  │",  
                                    r"5 │         | |   |     │",   
                                    r"6 │     .-=||  | |=-.   │",
                                    r"7 │     `-=#$%&%$#=-'   │",
                                    r"8 │         | ;  :|     │",
                                    r"9 │___.-#%&$@%#&#~,.____│",
                                    r"  └─────────────────────┘"]))
        io.expect_print("Player 1, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
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
                                ]))
        io.expect_print("Take a shot.")
        io.expect_print("Row:")
        io.provide("3")
        io.expect_print("Column:")
        io.provide("1")
        io.expect_print("Player 1, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( [r"    0 1 2 3 4 5 6 7 8 9  ",
                                    r"  ┌─────────────────────┐",
                                    r"0 │       HIT!          │",
                                    r"1 │              ( )    │",  
                                    r"2 │ BOOM!*  __*___|_ *  │",
                                    r"3 │   *  _ |_________*  │",
                                    r"4 │====| | |* SINK!   | │",
                                    r"5 │.--*------------*----│",
                                    r"6 │ \      *        *  /│",
                                    r"7 │  \________________/ │",
                                    r"8 │~~~~~~~~~~~~~~~~~~~~~│",
                                    r"9 │  ~~~~~~~~~~~~~~~~~~~│",
                                    r"  └─────────────────────┘"]))
        io.expect_print("Ship Sunk! You sunk a 2!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
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
                                ]))
        io.expect_print("Game Over!")
        io.expect_print("Player 1 Wins!")
        interface.run()
        
        

