import re
import tkinter as tk

class Keyboard():
    # TESTING CODE FOR THE COLORS
    _yellow = "#ACB22D"
    _green = "#268321"
    _white = "#F0F0F0"
    _light_gray = "#888888"
    _window_color = "#121212"
    _disable_color = "#3D3D3D"

    def __init__(self, window):
        # GUI keyboard characters inside the button / bindings for own keyboard
        self.window = window
        self.keys = [      
            {'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u' , 'i': 'i', 'o': 'o' , 'p': 'p'},
            {'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l'},
            {'Enter': '<Return>', 'z': 'z', 'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm', 'BackSpace': '<BackSpace>'}
        ]
        self.chars = [char for row in self.keys for char in row] # GUI keyboard characters
        self.binding_names = [row.get(char) for row in self.keys for char in row] # bindings for own keyboard
        self.keyboard_buttons = {} # GUI keyboard buttons
        
        self.enable_keys()
        self.keyboard()

    def disable_keys(self):
        for bind in self.binding_names:
            self.window.unbind(bind)
            self.keyboard_buttons[bind].config(state='disabled')

    def enable_keys(self):
        for binding_name in self.binding_names:
            # If the keyboard was made, and must be enabled again
            if(self.keyboard_buttons):
                self.keyboard_buttons[binding_name].config(state='normal')
    
            self.window.bind(binding_name, lambda char=binding_name: self.key_pressed(char))

            # If the character is a single letter, bind the uppercase too
            if(len(binding_name) == 1):
                self.window.bind(binding_name.upper(), lambda char=binding_name.upper(): self.key_pressed(char))

    def binding_to_char(self, bind):
        # Get all the binding characters and get the binding character of the bind
        binding_names = list(map(lambda binding_name: re.sub("[<>]", "", binding_name.lower()), self.binding_names))
        binding_name = bind.keysym.lower()
        
        return self.chars[binding_names.index(binding_name)] # Return the keyboard character of the bind

    def key_pressed(self, binding):
        # Character of the key that was pressed
        char = binding if isinstance(binding, str) else self.binding_to_char(binding) 
        char = char.lower()

        print(char) # TEST

    def keyboard(self):
        # Frame for the keyboard
        keyboard_frame = tk.Frame(
            self.window,
            bg=self._window_color, 
        )

        # For every keyboard row
        for row, row_chars in enumerate(self.keys):
            # Frame for the keyboard row
            row_frame = tk.Frame(
                keyboard_frame, 
                pady=3,
                bg=self._window_color,
            )
            row_frame.grid()

            # Keyboard button for each key
            for col, char in enumerate(row_chars):
                button = tk.Button(
                    row_frame, 
                    text=char.upper(),
                    command=lambda char=char: self.key_pressed(char),
                )
                button.grid(
                    row=row, 
                    column=col, 
                    padx=3,
                )  
                self.standard_button_styling(button, char) # Add the button styling

                # Add the button to the dictionary
                binding_name = self.keys[row][char]
                self.keyboard_buttons[binding_name] = button
            
            keyboard_frame.grid() # Place the keyboard on the window

    def get_button(self, char:str):
        return self.keyboard_buttons[char]

    def char_incorrect(self, char:str):
        self.get_button(char).config(
            background=self._disable_color,
        )
        
    def char_incorrect_position(self, char:str):
        self.get_button(char).config(
            background=self._yellow,
        )

    def standard_button_styling(self, button, char):
        big_keys = ['enter', 'backspace'] # Keys that are bigger on the keyboard
        width = 15 if char.lower() in big_keys else 10

        button.config(
            width=width,
            bg=self._light_gray,
            fg=self._white,
        )