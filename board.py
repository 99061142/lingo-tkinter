import tkinter as tk
from tkinter import ttk
import word

class Board():
    def __init__(self, window):
        self.window = window
        self._max_rounds = 5
        self._current_round = 1
        self._word = word.random_word()
        self.stringvars = [[tk.StringVar() for i in range(self.get_word_length())] for i in range(self._max_rounds)] # Characters in the board
        self.all_word_guesses = {}
        self.board() # Create the board

    def board(self):
        # Whole board frame
        self.board_frame = tk.Frame(
            self.window, 
            bg=self.window._window_color, 
            pady=25,
        )

        # For every round
        for row in range(self._max_rounds):
            # Frame for the word row
            board_row = tk.Frame(
                self.board_frame,
                bg=self.window._window_color, 
                pady=3,
            )
            board_row.grid()

            for col in range(self.get_word_length()):
                label = ttk.Label(
                    board_row, 
                    textvariable=self.stringvars[row][col], 
                    font=("Helvetica 15"), 
                    background="#565758", 
                    foreground=self.window._white, 
                    anchor="center",
                )
                label.grid(
                    row=row,
                    column=col, 
                    ipadx=15, 
                    ipady=10, 
                    padx=3,
                )
        self.board_frame.grid() # Place the board on the window 

    def get_word_length(self) -> int:
        return len(self._word)

    def get_row_word(self) -> list:
        return [char.get() for char in self.stringvars[self._current_round - 1]] # Word inside the current row

    def key_pressed(self, char:str):
        # add the character if the world is not fully guessed
        if('' in self.get_row_word()):
            empty_index = self.get_row_word().index('') 
            self.stringvars[self._current_round - 1][empty_index].set(char)

    def word_guessed(self) -> bool:
        return self.get_row_word() == self._word

    def enter_pressed(self) -> bool:
        # If all the columns are guessed and the word is real
        if('' not in self.get_row_word() and word.real_word(self.get_row_word())):
            # Add the word to the list of guessed words
            round_name = f"Round_{self._current_round}"
            self.all_word_guesses[round_name] = ''.join(self.get_row_word())
            
            self._current_round += 1 # Go to the next round
            return True
        return False

    def backspace_pressed(self):
        # Delete the last character in the current row
        index = self.get_word_length() if('' not in self.get_row_word()) else self.get_row_word().index('')        
        self.stringvars[self._current_round - 1][index - 1].set('')


    def create_end_info(self):  
        guessed_correctly = list(self.all_word_guesses)[-1] == self._word
        tries = self._current_round if (guessed_correctly) else self._current_round - 1

        # Game info to store
        game = {   
            "game_id": self.window.get_player_games() + 1, 
            "correct_word": self._word,
            "all_word_guesses": self.all_word_guesses,
            "guessed_correctly": guessed_correctly,
            "tries": tries,
        }
        self.window.add_player_game(game) # Add the game info