import tkinter as tk
from tkinter import ttk
from random_word import RandomWords
from tkinter import messagebox

import enchant

class Window(tk.Tk):
    _bg = "#121212"
    _labels = []
    _keyboard_buttons = []
    _keyboard_keys = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u' ,'i' ,'o' ,'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['Enter', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'BackSpace']
    ]
    _bindings_name = []

    def __init__(self):
        super().__init__() # "self" gets changed to the tkinter module

        # window for the game
        self.game_window_frame = tk.Frame(self, bg=self._bg)
        self.board_frame = tk.Frame(self.game_window_frame, bg=self._bg, pady=25)
        self.title("Lingo")
        self.configure(background=self._bg)
        self.geometry("1250x650")
        self.board()
        self.enable_keyboard() # Add the keyboard

    def board(self):    
        self.board_frame.pack()    

        # For every chance the user has to guess the word
        for row in range(self._chances):
            # Frame for the word row
            board_row = tk.Frame(self.board_frame, bg=self._bg, pady=3)
            board_row.grid()

            guessed_row_word = []
            row_labels = []

            # For every character inside the word
            for col in range(self.word_length):
                # Let the user change the text inside the label
                character_guess = tk.StringVar()
                guessed_row_word.append(character_guess)

                # Label that shows the key the user guessed
                label = ttk.Label(board_row, textvariable=character_guess, font=("Helvetica 15"), background='#565758', foreground='white', anchor='center')
                label.grid(row=row, column=col, ipadx=15, ipady=10, padx=3)
                row_labels.append(label)
            
            self._labels.append(row_labels)
            self._board.append(guessed_row_word)

    def keyboard(self):
        # Frame for the keyboard
        keyboard_frame = tk.Frame(self.game_window_frame, bg=self._bg)
        keyboard_frame.pack()

        big_keys = ['enter', 'backspace'] # Keys that are bigger on the keyboard

        # For every row on the keyboard
        for row, row_keys in enumerate(self._keyboard_keys):
            # Frame for the row on the keyboard
            row_frame = tk.Frame(keyboard_frame, bg=self._bg, pady=3)
            row_frame.grid()

            # Add the button for each key
            for col, key in enumerate(row_keys):
                width = 15 if key.lower() in big_keys else 10

                button = tk.Button(
                    row_frame, 
                    text=key.upper(),
                    width=width,
                    bg='#888888',
                    fg='#F0F0F0',
                    command= lambda key=key: self.key_pressed(key.lower())
                )
                button.grid(row=row, column=col, padx=3)
                self._keyboard_buttons.append(button)

    def keyboard_bindings(self):
        # Add the binding for every key on the GUI keyboard
        for key_row in self._keyboard_keys:
            for key in key_row:
                if(key.lower() == "enter"): 
                    self.bind('<Return>', lambda event: self.key_pressed('enter')) # Add enter binding
                    self._bindings_name.append('<Return>') # Add binding name to list
                else:
                    # Add binding for every key on the keyboard
                    binding_name = '<%s>' %key if len(key) > 1 else key
                    self.bind(binding_name, lambda key=key: self.key_pressed(key.keysym.lower()))
                    self._bindings_name.append(binding_name) # Add binding name to list

                    # Add the uppercase binding for the key
                    if len(key) == 1:
                        self.bind(binding_name.upper(), lambda key=key: self.key_pressed(key.keysym.lower()))
    
    def disable_keyboard(self):
        # Disable every key on the GUI keyboard
        for key in self._keyboard_buttons:              
            key['command'] = ''

        # Unbind every key on the GUI keyboard
        for binding_name in self._bindings_name:
            self.unbind(binding_name)

            # Unbind the uppercase key
            if(len(binding_name) == 1):
                self.unbind(binding_name.upper())

    def enable_keyboard(self):
        # Create the keyboard
        if not self._keyboard_buttons:
            self.keyboard()
        else:
            # Change every key styling on the GUI keyboard to the starting phase
            for key in self._keyboard_buttons:
                key.config(bg='#888888')    

        self.keyboard_bindings() # Add every binding for the keys that are on the GUI keyboard 

    def error_message(self, message:str):
        # Show the error message, and delete it after 2 seconds
        label = tk.Label(self.board_frame, text=message, font=("Helvetica 15"), bg='white')
        label.grid(row=0)
        self.after(2000, label.destroy)

    def end_screen(self, won:bool):
        self.disable_keyboard()


        end_frame = tk.Frame(self.board_frame, bg='white', padx=25, pady=25)
        end_frame.grid(row=0)

        message = "You guessed the word correctly" if won else "The word was %s" %self._word

        # Label that shows if the user won, or the word if the user lost        
        tk.Label(end_frame, text=message, font=("Helvetica 15"), anchor='center', bg='white', pady=25).grid()

        # Button to play again
        button = tk.Button(
            end_frame, 
            text='Play Again',
            font=("Helvetica 15 bold"),
        ).grid(sticky='NESW')
    
    def start(self):
        # Show the game
        self.game_window_frame.pack()    
        self.mainloop()


class Game(Window):
    _word = RandomWords().get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=6, maxLength=6).lower()
    _chances = 6
    _board = []
    _guess = 0

    def start(self):
        super().start() # Starts the game

    def key_pressed(self, key:str):
        # For every character inside the row
        for i, guessed_key in enumerate(self._board[self._guess]):            
            if(key == "backspace"):
                # Delete the last character that was guessed in the row
                self._board[self._guess][self.firstly_empty_column - 1].set('')
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
                    self.end_screen(True)
                else:
                    self._guess += 1 # Go to the next row

                    # When all the guesses are taken
                    if self._guess == self._chances:
                        self.end_screen(False)

                break

            # Add the pressed key at an empty column (if possible)
            if(not guessed_key.get()):
                # Change the character inside the row to the key the user has guessed
                self._board[self._guess][i].set(key)
                break
    
    def show_corrections(self):
        guessed_word = list(self.guessed_word)

        # Loop through the guessed / correct word
        for i, (guessed_character, character) in enumerate(zip(self.guessed_word, self._word)):
            # Change the label color to GREEN if the character is on the correct position
            if(guessed_character == character):
                guessed_word.remove(guessed_character)
                self._labels[self._guess][i].config(background='#268321') # Update row column styling
                self.change_key_styling(guessed_character, '#268321') # Update keyboard key styling

            # Change the label color to YELLOW if the character is in the word, but not on the correct position
            elif(guessed_character in self._word):
                guessed_word.remove(guessed_character)
                self._labels[self._guess][i].config(background='#ACB22D') # Update row column styling
                self.change_key_styling(guessed_character, '#ACB22D') # Update keyboard key styling
            else:
                self.change_key_styling(guessed_character) # Update keyboard key styling

    def change_key_styling(self, character:str, bg:str=None):
        # For every key on the keyboard
        for key in self._keyboard_buttons:
            key_name = key['text'].lower()
            # Change the background of the key when the guessed character is in the word
            if key_name == character:
                if bg:
                    key.config(bg=bg)
                else:
                    key.config(bg='#3D3D3D') # Disable the key when it's not in the word
                break

    @property
    def guessed_word(self) -> str:
        guessed_word = [character.get() for character in self._board[self._guess]] # Word the user has guessed
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
        for i, guessed_key in enumerate(self._board[self._guess]):
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