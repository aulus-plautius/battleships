import sys
from lib.players import Players
from lib.board import Board
from lib.user_interface import UserInterface


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)


io = TerminalIO()
user_interface = UserInterface(io, Players())
user_interface.run()
