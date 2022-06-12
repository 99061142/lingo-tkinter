from window import Window
import word
import tkinter as tk
from tkinter import ttk


class Board(Window):
    def __init__(self):
        super().__init__()
        self.new_game()

    def set_new_word(self):
        self._word = word.random_word()

    def set_board_columns_chars(self):
        self._board_columns_chars = [[tk.StringVar() for i in range(self.get_word_length())] for i in range(self.max_rounds)]

    def new_game(self):
        self.set_new_word()
        self.set_board_columns_chars()
        self.board()

    def board(self):
        # Delete the columns inside the board if the board already exitst, else create a new board
        try:
            for widget in self._board_frame.winfo_children():
                widget.destroy()
            board_frame = self._board_frame
        except AttributeError:
            board_frame = tk.Frame(
                self, 
                bg=self._window_color, 
                pady=25,
            )
            board_frame.grid()
            self._board_frame = board_frame

        # For every round
        for row in range(self.max_rounds):
            # Frame for the word row
            board_row = tk.Frame(
                board_frame,
                bg=self._window_color, 
                pady=3,
            )
            board_row.grid()

            for col in range(self.get_word_length()):
                    # Create the column inside the row
                    label = ttk.Label(
                        board_row, 
                        textvariable=self._board_columns_chars[row][col], 
                        font=("Helvetica 15"), 
                        background="#565758", 
                        foreground=self._white, 
                        anchor="center",
                    )
                    label.grid(
                        row=row,
                        column=col, 
                        ipadx=15, 
                        ipady=10, 
                        padx=3,
                    )