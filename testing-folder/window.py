from topHierachy import Type
import tkinter as tk
import word


class Window(tk.Tk, metaclass=Type):
    # All colors for the application
    _window_color = "#121212"
    _green = "#268321"
    _white = "#F0F0F0"
    _red = "#FF0000"
    _light_gray = "#888888"
    _key_incorrect_position = "#ACB22D"
    _key_incorrect = "#3D3D3D"
    
    def __init__(self):
        super().__init__()

        # VALUES FOR THE KEYBOARD
        # GUI keyboard characters / binding events for own keyboard
        self.keyboard_keys = [      
            {'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u' , 'i': 'i', 'o': 'o' , 'p': 'p'},
            {'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l'},
            {'Enter': '<Return>', 'z': 'z', 'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm', 'BackSpace': '<BackSpace>'}
        ]
        self.keyboard_chars = [char for row in self.keyboard_keys for char in row]
        self.keyboard_buttons = {}

        # VALUES FOR THE BOARD
        self.round = 1
        self.max_rounds = 5
        self._word = None
        self._board_columns_chars = None

        # VALUES FOR THE WINDOW
        self.binding_events = [row.get(char) for row in self.keyboard_keys for char in row]

        self.window_config()
        self.enable_binding_events()

    def window_config(self):
        self.title("Wordle clone")
        self.geometry("1000x500")

        self.config(
            background=self._window_color,
        )

    def get_word_length(self) -> int:
        return len(self._word)

    def word_guessed(self) -> bool:
        return self.get_current_word() == self._word

    def binding_event_to_char(self, event) -> str:
        return self.keyboard_chars[self.binding_events.index(event)]

    def enable_binding_events(self):
        for event in self.binding_events:
            char = self.binding_event_to_char(event).lower()
            self.bind(event, lambda event, char=char: self.key_pressed(char))

            # Bind the uppercase character too
            if(len(event) == 1):
                self.bind(event.upper(), lambda event, char=char: self.key_pressed(char))

    def disable_binding_events(self):
        for event in self.binding_events:
            self.unbind(event)

            # Unbind the uppercase character too
            if(len(event) == 1):
                self.unbind(event.upper())

    def key_pressed(self, char:str):
        if(char == "enter"):
            self.enter_pressed()
        elif(char == "backspace"):
            self.backspace_pressed()
        else:
            self.char_pressed(char)

    def char_pressed(self, char:str):
        index = self.get_first_empty_index()
        if(index != None):
            self.add_char_to_board(index, char)
    
    def enter_pressed(self):
        if(not word.real_word(self.get_current_word())):
            pass # Show error message
        elif(self.round == self.max_rounds):  
            pass # end game
        elif(self.word_guessed()):
            pass # end game
        else:
            self.round += 1

    def backspace_pressed(self):
        index = self.get_first_empty_index()
        if(index != 0):
            index = self.get_word_length() if(index == None) else index
            self.del_char_from_board(index)

    def del_char_from_board(self, index:int):       
        self._board_columns_chars[self.round - 1][index - 1].set('')

    def add_char_to_board(self, index:int, char:str):
        self._board_columns_chars[self.round - 1][index].set(char)

    def get_first_empty_index(self):
        word_list = self.get_current_word_list()
    
        if('' in word_list):
            return word_list.index('') 

    def get_current_word_list(self):
        return [char.get() for char in self._board_columns_chars[self.round - 1]]

    def get_current_word(self):
        return ''.join(self.get_current_word_list())