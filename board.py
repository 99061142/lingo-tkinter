from window import Window
import word
import tkinter as tk
from tkinter import ttk


class Board(Window):
    def __init__(self): 
        super().__init__()
        self.round = 1
        self.max_rounds = 5
        self._board_columns_chars = None
        self._board_frame = None
        self.word = None
        self.word_guesses = []
        self.new_game()

    def board(self):
        self.create_board_frame()   
        self.create_board_rows()

    def get_current_word_list(self) -> list:
        return [char.get() for char in self._board_columns_chars[self.round - 1]] # Current row word list in the board

    def get_current_word(self) -> str:
        return ''.join(self.get_current_word_list()) # Current row word in the board

    def set_new_word(self):
        self._word = word.random_word()

    def get_word_length(self) -> int:
        return len(self._word)

    def word_guessed(self) -> bool:
        return self.get_current_word() == self._word

    def set_board_columns_chars(self):
        self._board_columns_chars = [[tk.StringVar() for i in range(self.get_word_length())] for i in range(self.max_rounds)]

    def new_game(self):
        self.set_new_word()
        self.set_board_columns_chars()
        self.board()

    def create_board_frame(self):
        # Delete the columns inside the board if the board already exitst, else create a new board
        try:
            for widget in self._board_frame.winfo_children():
                widget.destroy()
        except AttributeError:
            board_frame = tk.Frame(
                self, 
                bg=self._window_color, 
                pady=25,
            )
            board_frame.grid(row=0)
            self._board_frame = board_frame

    def create_board_rows(self): 
        # For every round
        for row in range(self.max_rounds):
            board_row = tk.Frame(
                self._board_frame,
                bg=self._window_color, 
                pady=3,
            )
            board_row.grid()

            for col in range(self.get_word_length()):
                    # Create a column for every character
                    ttk.Label(
                        board_row, 
                        textvariable=self._board_columns_chars[row][col], 
                        font=("Helvetica 15"), 
                        background=self._column_background, 
                        foreground=self._white, 
                        anchor="center",
                    ).grid(
                        row=row,
                        column=col, 
                        ipadx=15, 
                        ipady=10, 
                        padx=3,
                    )

    def del_char_from_board(self, index:int):       
        self._board_columns_chars[self.round - 1][index - 1].set('')

    def add_char_to_board(self, index:int, char:str):
        self._board_columns_chars[self.round - 1][index].set(char)

    def get_first_empty_index(self):
        word_list = self.get_current_word_list()
    
        if('' in word_list):
            return word_list.index('') 