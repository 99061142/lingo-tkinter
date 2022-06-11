import tkinter as tk
from board import Board
from keyboard import Keyboard
import json

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

        self.get_player_games()
    
    def get_player_games(self) -> int:
        with open('scores.json', "r") as file:
            data = json.load(file)
        file.close()

        return len(data)

    def add_player_game(self, game:dict):
        with open('scores.json', "r") as file:
            data = json.load(file)
        file.close()

        data.append(game)

        with open('scores.json', "w") as file:
            json.dump(data, file)

    def start(self):
        board = Board(self)
        Keyboard(self, board)
        self.mainloop()




if __name__ == "__main__":
    App().start()