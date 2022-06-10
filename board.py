import tkinter as tk
from tkinter import ttk
import word

class Board():
    def __init__(self, window):
        self.window = window
        self.max_rounds = 5
        self._word = word.random_word()
        self.word_length = len(self._word)
        self.stringvars = [[tk.StringVar() for i in range(self.word_length)] for i in range(self.max_rounds)] # Characters in the board
        self.labels = []

        self.board()

    def board(self):
        # Whole board frame
        self.board_frame = tk.Frame(
            self.window, 
            bg=self.window._window_color, 
            pady=25
        )

        # For every round
        for row in range(self.max_rounds):
            # Frame for the word row
            board_row = tk.Frame(
                self.board_frame,
                bg=self.window._window_color, 
                pady=3
            )
            board_row.grid()

            for col in range(self.word_length):
                character = tk.StringVar() # Let the user change the character inside the label

                label = ttk.Label(
                    board_row, 
                    textvariable=character, 
                    font=("Helvetica 15"), 
                    background='#565758', 
                    foreground=self.window._white, 
                    anchor='center'
                )
                label.grid(
                    row=row,
                    column=col, 
                    ipadx=15, 
                    ipady=10, 
                    padx=3
                )
                
                self.stringvars[row].append(character) # Add the stringvar to the list
        self.board_frame.grid() # Place the board on the window