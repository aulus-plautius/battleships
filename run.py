import sys
from lib.players import Players
from lib.format_board import FormatBoard
from lib.user_interface import UserInterface


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)


io = TerminalIO()
user_interface = UserInterface(io)
user_interface.run()
