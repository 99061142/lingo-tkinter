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
        self.board_labels = [{} for i in range(self.max_rounds)]
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
        self.word_guesses = []
        self.board_labels = [{} for i in range(self.max_rounds)]
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
                label_frame = tk.Frame(
                    board_row, 
                    width=50, 
                    height=50,
                    background=self._column_background, 
                )
                label_frame.pack_propagate(0) # Set fixed size
                
                label = ttk.Label(
                    label_frame,
                    textvariable=self._board_columns_chars[row][col],
                    font=("Helvetica 15"),  
                    background=self._column_background, 
                    foreground=self._white
                )
                label.pack(expand=True)
    
                label_frame.grid(
                    row=row, 
                    column=col, 
                    padx=5
                )
                self.board_labels[row][col] = {
                    "label_frame": label_frame,
                    "label": label,
                }
                

    def del_char_from_board(self, index:int):       
        self._board_columns_chars[self.round - 1][index - 1].set('')

    def add_char_to_board(self, index:int, char:str):
        self._board_columns_chars[self.round - 1][index].set(char)

    def get_first_empty_index(self):
        word_list = self.get_current_word_list()
    
        if('' in word_list):
            return word_list.index('') 

    def check_characters(self):
        correct_word = self._word

        for i, (correct_char, char) in enumerate(zip(self._word, self.get_current_word())):            
            if char == correct_char:
                self.button_config(char, self._green)
                self.label_config(i, self._green)
            elif char in correct_word:
                self.button_config(char, self._yellow)
                self.label_config(i, self._yellow)
            else:
                self.button_config(char, self._incorrect)
                self.label_config(i, self._incorrect)

            if(char in correct_word):
                correct_word = correct_word.replace(char, '')

    def label_config(self, index:int, color:str):
        for label_data in self.board_labels[self.round - 1][index].values():
            label_data.config(
                background=color,
            )