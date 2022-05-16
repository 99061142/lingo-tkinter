import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import choice

class Window(tk.Tk):
    #Labels
    _labels = []
    _label_characters = []

    #Keyboard keys
    _keyboard_bindings = {}
    _keyboard_keys = {}
    _keyboard_characters = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u' ,'i' ,'o' ,'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['Enter', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'BackSpace']
    ]
    
    # Frames
    _end_frame = None
    _board_frame = None

    # Colors
    _yellow = "#ACB22D"
    _green = "#268321"
    _white = "#F0F0F0"
    _light_gray = "#888888"
    _window_color = "#121212"
    _disable_color = "#3D3D3D"

    def __init__(self):
        super().__init__() # "self" gets changed to the tkinter module
        self._word = self.random_word # Get a random word to begin the game

        # Game window
        self.title("Lingo")
        self.configure(background=self._window_color)
        self.geometry("1250x650")
        
        self.create_board() # Board
        self.create_keyboard() # Keyboard GUI
        self.add_keyboard_bindings() # Normal keyboard bindings

    def create_board(self):    
        # Board frame
        self.board_frame = tk.Frame(
            self, 
            bg=self._window_color, 
            pady=25
        )

        # Add a row For every round
        for row in range(self.max_rounds):
            # Frame for the word row
            board_row = tk.Frame(
                self.board_frame,
                bg=self._window_color, 
                pady=3
            )
            board_row.grid()

            row_labels = [] # List with every column inside the row
            row_label_characters = [] # List to change the characters inside the row

            # For every column
            for col in range(self.word_length):
                # Let the user change the text inside the label
                character_guess = tk.StringVar()
                row_label_characters.append(character_guess)

                # Column for the character
                label = ttk.Label(
                    board_row, 
                    textvariable=character_guess, 
                    font=("Helvetica 15"), 
                    background='#565758', 
                    foreground='white', 
                    anchor='center'
                )
                label.grid(
                    row=row,
                    column=col, 
                    ipadx=15, 
                    ipady=10, 
                    padx=3
                )
                
                row_labels.append(label)

            self.add_label_characters(row_label_characters)
            self.add_row_labels(row_labels)

    @property
    def label_characters(self):
        return self._label_characters

    
    def add_label_characters(self, row_labels_characters:list):
        self._label_characters.append(row_labels_characters)


    def create_keyboard(self):
        # Frame for the keyboard
        self.keyboard_frame = tk.Frame(
            self, 
            bg=self._window_color
        )

        # For every keyboard row
        for row, row_keys in enumerate(self.keyboard_buttons):
            # Frame for the keyboard row
            row_frame = tk.Frame(
                self.keyboard_frame, 
                bg=self._window_color, 
                pady=3
            )
            row_frame.grid()

            # Add the button for each key
            for col, key in enumerate(row_keys):
                button = tk.Button(
                    row_frame, 
                    text=key.upper()
                )
                button.grid(
                    row=row, 
                    column=col, 
                    padx=3
                )

                self.add_keyboard_key(key, button)

        self.keyboard_config() 
    
    def keyboard_config(self):
        # For every key on the keyboard
        for key_character in self.keyboard_keys:
            key = self.keyboard_keys[key_character] # Key itself
            key_text = key['text'].lower() # Character
            big_keys = ['enter', 'backspace'] # Keys that are bigger on the keyboard
            width = 15 if key_text in big_keys else 10 # Width of the key

            key.config(
                width=width,
                bg=self._light_gray,
                fg=self._white,
                command=lambda key_text=key_text: self.key_pressed(key_text)
            )

    def add_keyboard_bindings(self):
        # Binding for every key on the GUI keyboard
        for key in self.keyboard_keys:    
            if(key.lower() == "enter"): 
                # Create binding and add it to the bindings list
                binding = self.bind('<Return>', lambda event: self.key_pressed('enter'))
                self.add_keyboard_binding('enter', binding)
            else:
                binding_name = '<%s>' %key if len(key) > 1 else key

                # Create binding and add it to the bindings list
                binding = self.bind(binding_name, lambda key=key: self.key_pressed(key.keysym.lower()))
                self.add_keyboard_binding(key.lower(), binding)

                # Add uppercase binding
                if len(key) == 1:
                    # Create binding and add it to the bindings list
                    binding = self.bind(binding_name.upper(), lambda key=key: self.key_pressed(key.keysym.lower()))
                    self.add_keyboard_binding(key.lower(), binding)

    def error_message(self, message:str):
        # Show the error message, and delete it after 2 seconds
        label = tk.Label(self.board_frame, text=message, font=("Helvetica 15"), bg='white')
        label.grid(row=0)
        self.after(2000, label.destroy)

    @property
    def labels(self) -> list:
        return self._labels # All the labels on the board

    def add_row_labels(self, row_labels:list):
        self._labels.append(row_labels) # Add row with labels
    
    @property
    def keyboard_buttons(self):
        return self._keyboard_characters # Rows with keyboard characters

    @property
    def keyboard_keys(self):
        return self._keyboard_keys # Rows with keyboard Keys (tkinter button)
    
    @property 
    def keyboard_bindings(self):
        return self._keyboard_bindings # Bindings for every key that's on the GUI keyboard

    def add_keyboard_binding(self, character, binding):
        # Add the binding inside the list of the character value
        try:
            self._keyboard_bindings[character]
        except KeyError:
            self._keyboard_bindings[character] = []
        finally:
            self._keyboard_bindings[character].append(binding)
        
    def add_keyboard_key(self, key, button):    
        self._keyboard_keys[key] = button # Add the binding for the key that's on the GUI keyboard
    
    @property
    def board_frame(self):
        return self._board_frame

    @board_frame.setter
    def board_frame(self, frame):
        self._board_frame = frame
        self._board_frame.pack()

    @board_frame.deleter
    def board_frame(self):
        self._board_frame.destroy()

    @property
    def keyboard_frame(self):
        return self._keyboard_frame

    @keyboard_frame.setter
    def keyboard_frame(self, frame):
        self._keyboard_frame = frame
        self._keyboard_frame.pack()

    @keyboard_frame.deleter
    def keyboard_frame(self):
        self.keyboard_frame.destroy()

    """
    def clear_board(self):
        for row, board_row in enumerate(self._labels):
            for col, label in enumerate(board_row):
                label_character = self._board[row][col]
                
                if label_character:
                    label_character.set('')
                    label.config(background='#565758')

    def enable_keyboard(self):
        # Create the keyboard
        if not len(self._keyboard_characters):
            self.keyboard()
        else:
            self.keyboard_config()  

        self.keyboard_bindings() # Add every binding for the keys that are on the GUI keyboard 
    
    def disable_keyboard(self):
        # Disable every key on the GUI keyboard
        for key in self._keyboard_characters:              
            key['command'] = ''

        # Unbind every key on the GUI keyboard
        for binding_name in self._bindings_name:
            self.unbind(binding_name)

            # Unbind the uppercase key
            if(len(binding_name) == 1):
                self.unbind(binding_name.upper())

    def end_screen(self, won:bool):
        end_frame = tk.Frame(self.board_frame, bg='white', padx=25, pady=25)
        end_frame.grid(row=0)
        self.end_frame = end_frame

        # Label that shows if the user won, or the word if the user lost 
        message = "You guessed the word correctly" if won else "The word was %s" %self._word
        
        tk.Label(
            end_frame, 
            text=message, 
            font=('Helvetica 15'), 
            anchor='center', 
            bg='white', 
            pady=25
        ).grid()

        # Button to play again
        button = tk.Button(
            end_frame, 
            text='Play Again',
            font=('Helvetica 15 bold'),
            command= lambda: self.play_again()
        ).grid(sticky='NESW')
    
    @property
    def end_frame(self):
        return this._end_frame

    @end_frame.setter
    def end_frame(self, frame):
        self._end_frame = frame

    @end_frame.deleter
    def end_frame(self):
            self._end_frame.destroy()
    """


class Game(Window):
    _word = None
    _round = 0
    _max_rounds = 6

    @property
    def max_rounds(self):
        return self._max_rounds # Max rounds to guess the word

    @property
    def round(self) -> int:
        return self._round # Round the user is on

    @property
    def guessed_columns(self) -> int:
        # Get the amount of columns the user already guessed
        for i, character in enumerate(self.label_characters[self.round]):
            if not character.get():
                return i
        return len(self.labels[self.round])

    @property
    def word_length(self) -> int:
        return len(self._word)

    @property 
    def random_word(self):
        return choice(self.possible_words) # Get an random word


    @property
    def open_columns(self) -> bool:
        return self.guessed_columns != self.word_length # If the user can add more characters

    @property
    def current_row_word(self) -> str:
        # Word the user made
        row_word = [label['text'] for label in self.labels[self.round]]        
        row_word = ''.join(row_word)

        return row_word

    @property
    def possible_words(self) -> list:
        return open('words.txt','r').read().splitlines()

    @property
    def real_word(self) -> bool:
        return self.current_row_word in self.possible_words # If word is in the word list

    @property
    def word_guessed(self) -> bool:
        return self.current_row_word == self._word # If the user guessed the word correctly

    def next_round(self):
        # When the game is over
        if(self.round == self._max_rounds):
            pass
        else:
            self.show_corrections() # Show on the keyboard if the key was on the correct position / in the word at an other position
            self._round += 1 # Go to the next round

    def key_pressed(self, key:str) -> None:
        if key == "enter":    
            # If not every column was filled in
            if(self.guessed_columns != self.word_length):
                self.error_message("Not enough letters")
            else: 
                # If the word is real
                if self.real_word:
                    # If guessed correctly
                    if self.word_guessed:
                        pass
                    else:
                        self.next_round() # Go to the next round
                    return
                
                else:
                    self.error_message("Not in word list")
            return
        
        elif key == "backspace":
            # If the first column isn't empty
            if(self.guessed_columns):
                self.label_characters[self.round][self.guessed_columns - 1].set('') # Delete the last character that was added
            return

        # Add character if possible
        if self.open_columns:
            self.label_characters[self.round][self.guessed_columns].set(key)
            return
    
    def show_corrections(self):
        guessed_word = list(self.current_row_word) # Word the user has guessed

        # Loop through the guessed / correct word
        for i, (guessed_character, character) in enumerate(zip(self.current_row_word, self._word)):
            # Correct position
            if(guessed_character == character):
                background_color = self._green

            # Not correct position but in word
            elif(guessed_character in self._word):
                background_color = self._yellow
            
            # Correct position / not correct position but in word
            if(guessed_character == character or guessed_character in self._word):
                guessed_word.remove(guessed_character)
                self.labels[self.round][i].config(background=background_color) # Column styling
                self.change_key_styling(guessed_character, background_color) # Keyboard key styling
            
            # Not in word
            if guessed_character not in self._word:
                self.change_key_styling(guessed_character) # Keyboard key styling

    def change_key_styling(self, character:str, bg:str=None):        
        key = self.keyboard_keys[character] # Key on the GUI keyboard

        # If character was in word
        if bg:
            key.config(bg=bg) # Change key background
        else:
            key.config(bg=self._disable_color) # Change key background

    def start(self):  
        self.mainloop() # Start / show the game
    
    
    """
    def game_over(self, won:bool):
        self.disable_keyboard()
        self.end_screen(won)

    def play_again(self):
        del self.end_frame
        self.enable_keyboard()
        self.clear_board()
        self._guess = 0

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
    """




if __name__ == "__main__":
    game = Game()
    game.start()