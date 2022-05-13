import tkinter as tk
from tkinter import ttk
from random_word import RandomWords

class Window(tk.Tk):
    _bg = "#121212"

    def __init__(self):
        super().__init__() # "self" gets changed to the tkinter module

        # window for the game
        self.game_window = tk.Frame(self, bg=self._bg)
        self.title("Lingo")
        self.configure(background=self._bg)
        self.geometry("1000x500")
        self.keyboard() # Add the keyboard
        

    def keyboard(self):
        # Frame for the keyboard
        keyboard_frame = tk.Frame(self.game_window, bg=self._bg)
        keyboard_frame.pack()
    
        # Keys on the keyboard
        keys = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u' ,'i' ,'o' ,'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['enter', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'backspace']
        ]
        big_keys = ['enter', 'backspace'] # Keys that are bigger on the keyboard

        # For every row on the keyboard
        for row, row_keys in enumerate(keys):
            # Frame for the row on the keyboard
            row_frame = tk.Frame(keyboard_frame, bg=self._bg)
            row_frame.grid()

            # Add the button for each key
            for col, key in enumerate(row_keys):
                width = 15 if key in big_keys else 10

                button = tk.Button(
                    row_frame, 
                    text=key.upper(),
                    width=width,
                    bg='#888888',
                    fg='#F0F0F0'
                ).grid(row=row, column=col, padx=3, pady=3)

    def start(self):
        # Show the game
        self.game_window.pack()    
        self.mainloop()


class Game(Window):
    _word = RandomWords().get_random_word(hasDictionaryDef="true", minLength=4, maxLength=6)

    def start(self):
        super().start() # Starts the game




if __name__ == "__main__":
    game = Game()
    game.start()
