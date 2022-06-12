import tkinter as tk
from scores import Scores

class Window(tk.Tk, Scores):
    # All colors for the application
    _window_color = "#121212"
    _green = "#268321"
    _white = "#F0F0F0"
    _red = "#FF0000"
    _light_gray = "#888888"
    _yellow = "#ACB22D"
    _incorrect = "#3D3D3D"
    _column_background = "#565758"
    
    def __init__(self):
        super().__init__()
        self.keyboard_keys = [      
            {'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u' , 'i': 'i', 'o': 'o' , 'p': 'p'},
            {'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l'},
            {'Enter': '<Return>', 'z': 'z', 'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm', 'BackSpace': '<BackSpace>'}
        ]
        self.binding_events = [row.get(char) for row in self.keyboard_keys for char in row]
        self.window_config()

    def window_config(self):
        self.title("Wordle clone")
        self.geometry("1000x500")

        self.config(
            background=self._window_color,
        )

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