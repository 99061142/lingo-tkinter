from board import Board
from keyboard import Keyboard

class App(Keyboard, Board):
    def __init__(self):
        super().__init__()

    def start(self):
        self.mainloop()




if __name__ == "__main__":
    app = App()
    app.start()