import tkinter as tk
from board import Board
from keyboard import Keyboard

# IMPORT KEYBOARD FILE 
class App(tk.Tk):
    _window_color = "#121212"
    _green = "#268321"
    _white = "#F0F0F0"
    _light_gray = "#888888"
    _button_incorrect_position = "#ACB22D"
    _button_incorrect = "#3D3D3D"

    def __init__(self):
        super().__init__()
        self.title("Wordle clone")
        self.geometry("1000x500")

        self.config(
            background=self._window_color,
        )

    def start(self):
        board = Board(self)
        Keyboard(self, board)
        self.mainloop()




if __name__ == "__main__":
    App().start()