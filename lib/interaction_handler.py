class InteractionHandler:
    def __init__(self, io) -> None:
        self.io = io
    
    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()
    
    def _clear_terminal(self):
        print("\033c", end="")
        # pass
