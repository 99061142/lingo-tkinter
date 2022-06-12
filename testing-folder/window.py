from topHierachy import Type
import tkinter as tk

class Window(tk.Tk, metaclass=Type):
    # All colors for the application
    _window_color = "#121212"
    _green = "#268321"
    _white = "#F0F0F0"
    _red = "#FF0000"
    _light_gray = "#888888"
    _key_incorrect_position = "#ACB22D"
    _key_incorrect = "#3D3D3D"
    
    def __init__(self):
        super().__init__()
        self.window_config()

    def window_config(self):
        self.title("Wordle clone")
        self.geometry("1000x500")

        self.config(
            background=self._window_color,
        )