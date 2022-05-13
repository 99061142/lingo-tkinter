import tkinter as tk
from tkinter import ttk
from random_word import RandomWords
from tkinter import messagebox

class Window(tk.Tk):
    _bg = "#121212"

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

            # For every character inside the word
            for col in range(self.word_length):
                # Let the user change the text inside the label
                character_guess = tk.StringVar()
                guessed_row_word.append(character_guess)

                ttk.Label(board_row, textvariable=character_guess, font=("Helvetica 15"), anchor='center').grid(row=row, column=col, ipadx=15, ipady=10, padx=3) # Label that shows the key the user guessed

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
    _word = RandomWords().get_random_word(hasDictionaryDef="true", minLength=6, maxLength=6)
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
                # If the user guessed every column
                if(self.firstly_empty_column == self.word_length):
                    self.check_guessed_word()
                    self._guess += 1 # Go to the next row
                else:
                    self.error_message("Not enough letters") # Show the error message
                break

            # If the column is not already guessed (length of the word was not reached)
            if(not guessed_key.get()):
                # Change the character inside the row to the key the user has guessed
                self._guessed_words[self._guess][i].set(key)
                break
    
    def check_guessed_word(self):
        guessed_word = [x.get() for x in self._guessed_words[self._guess]] # Word the user has guessed

    
    @property
    def firstly_empty_column(self):
        # For every character inside the row
        for i, guessed_key in enumerate(self._guessed_words[self._guess]):
            # Return the index that's empty
            if(not guessed_key.get()):
                return i

        return self.word_length

    @property
    def word_length(self):
        return len(self._word)




if __name__ == "__main__":
    game = Game()
    game.start()