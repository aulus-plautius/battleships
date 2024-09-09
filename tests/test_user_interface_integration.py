import unittest

from lib.user_interface import UserInterface
from lib.ship import Ship
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock



class TestUserInterface(unittest.TestCase):
    def test_full_game_of_1_ship(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io)
        interface.players.players[0].unplaced_ships = [Ship(2)]
        interface.players.players[1].unplaced_ships = [Ship(2)]

        io.expect_print("Welcome to the game!")
        io.expect_print("Please enter player 1's name:")
        io.provide("joe")
        io.expect_print("Please enter player 2's name:")
        io.provide("harriet")
        io.expect_print("Joe, set up your ships first.")
        io.expect_print("This is your board:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · · · · · · · · · · │",
                                    "D │ · · · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · · · · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("You have these ships remaining: 2")
        io.expect_print("Place your ship: 2")
        # io.provide("6")
        # io.expect_print("Invalid ship, try again!")
        # io.expect_print("Which do you wish to place?")
        # io.provide("2")

        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("x")
        io.expect_print("Invalid orientation, try again!")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("x")
        io.expect_print("Invalid row, try again!")
        io.expect_print("Which row?")
        io.provide("C")
        io.expect_print("Which column?")
        io.provide("x")
        io.expect_print("Invalid column, try again!")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · S · · · · · · · · │",
                                    "D │ · S · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · · · · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Press enter to finish.")
        io.provide("")
# Harriet sets up their board -------------------------------------------------
        io.expect_print("Harriet, set up your ships first.")
        io.expect_print("This is your board:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · · · · · · · · · · │",
                                    "D │ · · · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · · · · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("You have these ships remaining: 2")
        io.expect_print("Place your ship: 2")
        # io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("f")
        io.expect_print("Which column?")
        io.provide("6")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · · · · · · · · · · │",
                                    "D │ · · · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · S S · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Press enter to finish.")
        io.provide("")
# game starts ------------------------------------------------------------------
        io.expect_print("Joe, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · · · · · · · · · · │",
                                    "D │ · · · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · · · · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Take a shot.")
        io.expect_print("Row:")
        io.provide("C")
        io.expect_print("Column:")
        io.provide("6")
        io.expect_print("Joe, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A |                     |",
                                    "B │       .-- .         │",
                                    "C │     .(     )        │",
                                    "D │   (       ))     _  │",
                                    "E │  _ `- __.'    . ` ) │",
                                    "F │  __ .  MISS! :(    )│",
                                    "G │(     '`. .  `(     )│",
                                    "H │(       ) )    ` _.' │",
                                    "I │ `_.:'-'             │",
                                    "J │~~~~~~~~~~~~~~~~~~~~~│",
                                    "  └─────────────────────┘"]))
        io.expect_print("Joe, your turn is over!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · · · · · · O · · · │",
                                    "D │ · · · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · · · · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Remaining enemy ships: 2")
        io.expect_print("Press enter to finish.")
        io.provide("")
        io.expect_print("Harriet, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · · · · · · · · · · │",
                                    "D │ · · · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · · · · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Take a shot.")
        io.expect_print("Row:")
        io.provide("C")
        io.expect_print("Column:")
        io.provide("1")
        io.expect_print("Harriet, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( [r"    0 1 2 3 4 5 6 7 8 9  ",
                                    r"  ┌─────────────────────┐",
                                    r"A │  _.-^^---....,,--_  │",
                                    r"B │_-                 -_│",
                                    r"C │<        HIT!      >)│",
                                    r"D │\.                 / │",
                                    r"E │  ```--. . , ; .--'  │",  
                                    r"F │         | |   |     │",   
                                    r"G │     .-=||  | |=-.   │",
                                    r"H │     `-=#$%&%$#=-'   │",
                                    r"I │         | ;  :|     │",
                                    r"J │___.-#%&$@%#&#~,.____│",
                                    r"  └─────────────────────┘"]))
        io.expect_print("Harriet, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · X · · · · · · · · │",
                                    "D │ · · · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · · · · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Take a shot.")
        io.expect_print("Row:")
        io.provide("D")
        io.expect_print("Column:")
        io.provide("1")
        io.expect_print("Harriet, its your turn!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( [r"    0 1 2 3 4 5 6 7 8 9  ",
                                    r"  ┌─────────────────────┐",
                                    r"A │       HIT!          │",
                                    r"B │              ( )    │",  
                                    r"C │ BOOM!*  __*___|_ *  │",
                                    r"D │   *  _ |_________*  │",
                                    r"E │====| | |* SINK!   | │",
                                    r"F │.--*------------*----│",
                                    r"G │ \      *        *  /│",
                                    r"H │  \________________/ │",
                                    r"I │~~~~~~~~~~~~~~~~~~~~~│",
                                    r"J │  ~~~~~~~~~~~~~~~~~~~│",
                                    r"  └─────────────────────┘"]))
        io.expect_print("Ship Sunk! You sunk a 2!")
        io.expect_print("Enemy ships:")
        io.expect_print("\n".join( ["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A │ · · · · · · · · · · │",
                                    "B │ · · · · · · · · · · │",
                                    "C │ · # · · · · · · · · │",
                                    "D │ · # · · · · · · · · │",
                                    "E │ · · · · · · · · · · │",
                                    "F │ · · · · · · · · · · │",
                                    "G │ · · · · · · · · · · │",
                                    "H │ · · · · · · · · · · │",
                                    "I │ · · · · · · · · · · │",
                                    "J │ · · · · · · · · · · │",
                                    "  └─────────────────────┘"
                                ]))
        io.expect_print("Game Over!")
        io.expect_print("Harriet wins!")
        interface.run()
        
        

