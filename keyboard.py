from window import Window
import tkinter as tk
import word

class Keyboard(Window):
    def __init__(self):
        super().__init__()
        self._keyboard_frame = None
        self.keyboard_chars = [char for row in self.keyboard_keys for char in row]
        self.keyboard_buttons = {}
        self.create_keyboard()
        self.enable_binding_events()

    def create_keyboard(self):
        self.create_keyboard_frame()
        self.create_keyboard_buttons()

    def create_keyboard_frame(self):
        # Frame for the keyboard
        keyboard_frame = tk.Frame(
            self,
            bg=self._window_color,
        )
        keyboard_frame.grid(row=1)
        self._keyboard_frame = keyboard_frame

    def create_keyboard_buttons(self):
        # For every keyboard row
        for row, row_chars in enumerate(self.keyboard_keys):
            # Frame for the keyboard row
            row_frame = tk.Frame(
                self._keyboard_frame, 
                pady=3,
                bg=self._window_color,
            )
            row_frame.grid()

            # Keyboard button for each key
            for col, char in enumerate(row_chars):
                big_keys = ['enter', 'backspace'] # Keys that are bigger on the keyboard
                width = 15 if char.lower() in big_keys else 10

                button = tk.Button(
                    row_frame, 
                    text=char.upper(),
                    command=lambda char=char: self.key_pressed(char),
                    width=width,
                )
                button.grid(
                    row=row, 
                    column=col, 
                    padx=3,
                )  
                self.standard_button_styling(button, char) # Button color styling

                # Add the button to the dictionary
                binding_name = self.keyboard_keys[row][char]
                self.keyboard_buttons[binding_name] = button

    def standard_button_styling(self, button, char:str):
            button.config(
                bg=self._light_gray,
                fg=self._white,
            )

    def button_config(self, char:str, color:str):
        self.keyboard_buttons[char].config(
            bg=color,
        )

    def key_pressed(self, char:str):
        if(char == "enter"):
            self.enter_pressed()
        elif(char == "backspace"):
            self.backspace_pressed()
        else:
            self.char_pressed(char)

    def char_pressed(self, char:str):
        index = self.get_first_empty_index()

        # If the row is not full
        if(index != None):
            self.add_char_to_board(index, char)
    
    def enter_pressed(self):
        if(self.get_first_empty_index() != None):
            self.show_error("The word is not complete")
        elif(not word.real_word(self.get_current_word())):
            self.show_error("The word is not in the word list")
        elif(self.round == self.max_rounds or self.word_guessed()):
            self.word_guesses.append(self.get_current_word())
            self.check_characters()
            self.game_over()
        else:
            self.word_guesses.append(self.get_current_word())
            self.check_characters()
            self.round += 1

    def backspace_pressed(self):
        index = self.get_first_empty_index()

        # If the row is not empty
        if(index != 0):
            index = self.get_word_length() if(index == None) else index
            self.del_char_from_board(index)

    def enable_keyboard(self):
        for button in self.keyboard_buttons.values():
            button.config(state="normal")

    def disable_keyboard(self):
        for button in self.keyboard_buttons.values():
            button.config(state="disabled")

    def binding_event_to_char(self, event) -> str:
        return self.keyboard_chars[self.binding_events.index(event)]

    def standard_keyboard_styling(self):
        for char, button in self.keyboard_buttons.items():
            self.standard_button_styling(button, char)