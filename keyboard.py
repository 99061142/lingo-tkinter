from window import Window
import tkinter as tk

class Keyboard(Window):
    def __init__(self):
        super().__init__()
        self.keyboard()

    def keyboard(self):
        # Frame for the keyboard
        keyboard_frame = tk.Frame(
            self,
            bg=self._window_color,
        )

        # For every keyboard row
        for row, row_chars in enumerate(self.keyboard_keys):
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
                binding_name = self.keyboard_keys[row][char]
                self.keyboard_buttons[binding_name] = button
            
            keyboard_frame.grid() # Place the keyboard on the window

    def standard_button_styling(self, button, char:str):
            big_keys = ['enter', 'backspace'] # Keys that are bigger on the keyboard
            width = 15 if char.lower() in big_keys else 10

            button.config(
                width=width,
                bg=self._light_gray,
                fg=self._white,
            )

    def char_incorrect(self, char:str):
        self.keyboard_buttons[char].config(
            background=self._key_incorrect,
        )

    def char_incorrect_position(self, char:str):
        self.keyboard_buttons[char].config(
            background=self._key_incorrect_position,
        )