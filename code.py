import tkinter as tk
from tkinter import ttk
from random_word import RandomWords
from tkinter import messagebox

import enchant

class Window(tk.Tk):
    _bg = "#121212"
    _labels = []

    def __init__(self):
        super().__init__() # "self" gets changed to the tkinter module

        # window for the game
        self.game_window_frame = tk.Frame(self, bg=self._bg)
        self.title("Lingo")
        self.configure(background=self._bg)
        self.geometry("1000x500")
        self.board()
        self.keyboard() # Add the keyboard
    
    def board(self):
        # Frame for the board 
        board_frame = tk.Frame(self.game_window_frame, bg=self._bg, pady=25)
        board_frame.pack()
        
        # For every chance the user has to guess the word
        for row in range(self._chances):
            # Frame for the word row
            board_row = tk.Frame(board_frame, bg=self._bg, pady=3)
            board_row.grid()

            guessed_row_word = []
            row_labels = []

            # For every character inside the word
            for col in range(self.word_length):
                # Let the user change the text inside the label
                character_guess = tk.StringVar()
                guessed_row_word.append(character_guess)

                # Label that shows the key the user guessed
                label = ttk.Label(board_row, textvariable=character_guess, font=("Helvetica 15"), anchor='center')
                label.grid(row=row, column=col, ipadx=15, ipady=10, padx=3)
                row_labels.append(label)
            
            self._labels.append(row_labels)
            self._guessed_words.append(guessed_row_word)

    def keyboard(self):
        # Frame for the keyboard
        keyboard_frame = tk.Frame(self.game_window_frame, bg=self._bg)
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
            row_frame = tk.Frame(keyboard_frame, bg=self._bg, pady=3)
            row_frame.grid()

            # Add the button for each key
            for col, key in enumerate(row_keys):
                width = 15 if key in big_keys else 10

                button = tk.Button(
                    row_frame, 
                    text=key.upper(),
                    width=width,
                    bg='#888888',
                    fg='#F0F0F0',
                    command= lambda key=key: self.key_pressed(key)
                ).grid(row=row, column=col, padx=3)

    def error_message(self, message:str):
        messagebox.showerror("", message) # Show the error message

    def start(self):
        # Show the game
        self.game_window_frame.pack()    
        self.mainloop()


class Game(Window):
    _word = RandomWords().get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=6, maxLength=6).lower()
    _chances = 6
    _guessed_words = []
    _guess = 0

    def start(self):
        super().start() # Starts the game

    def key_pressed(self, key:str):
        # For every character inside the row
        for i, guessed_key in enumerate(self._guessed_words[self._guess]):            
            if(key == "backspace"):
                # Delete the last character that was guessed in the row
                self._guessed_words[self._guess][self.firstly_empty_column - 1].set('')
                break
            
            elif(key == "enter"):
                # Show an error message if the user guessed every column
                if(self.firstly_empty_column != self.word_length):
                    self.error_message("Not enough letters")
                    break
    
                # Show an error message if the word is not real
                if(not self.real_word and not self.guessed_correctly):
                    self.error_message("Not in word list")
                    break
            
                self.show_corrections()

                # Show the end screen if the user guessed the word
                if(self.guessed_correctly):
                    pass
                else:
                    self._guess += 1 # Go to the next row
                break

            # Add the pressed key at an empty column (if possible)
            if(not guessed_key.get()):
                # Change the character inside the row to the key the user has guessed
                self._guessed_words[self._guess][i].set(key)
                break
    
    def show_corrections(self):
        guessed_word = list(self.guessed_word)

        # Loop through the guessed / correct word
        for i, (guessed_character, character) in enumerate(zip(self.guessed_word, self._word)):
            # Change the label color to GREEN if the character is on the correct position
            if(guessed_character == character):
                guessed_word.remove(guessed_character)
                self._labels[self._guess][i].config(background="green")

            # Change the label color to YELLOW if the character is in the word, but not on the correct position
            elif(guessed_character in self._word):
                guessed_word.remove(guessed_character)
                self._labels[self._guess][i].config(background="yellow")

    @property
    def guessed_word(self) -> str:
        guessed_word = [x.get() for x in self._guessed_words[self._guess]] # Word the user has guessed
        return ''.join(guessed_word)
    
    @property
    def real_word(self) -> bool:
        return enchant.Dict("en_US").check(self.guessed_word)

    @property
    def guessed_correctly(self) -> bool:
        return self.guessed_word == self._word

    @property
    def firstly_empty_column(self) -> int:
        # For every character inside the row
        for i, guessed_key in enumerate(self._guessed_words[self._guess]):
            # Return the index that's empty
            if(not guessed_key.get()):
                return i

        return self.word_length

    @property
    def word_length(self) -> int:
        return len(self._word)




if __name__ == "__main__":
    game = Game()
    game.start()