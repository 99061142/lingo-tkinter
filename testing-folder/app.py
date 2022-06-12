from board import Board
from keyboard import Keyboard

class App(Board, Keyboard):
    def __init__(self):
        super().__init__()


    def start(self):
        pass

    def restart(self):
        pass




if __name__ == "__main__":
    app = App()
    app.start()