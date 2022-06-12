import tkinter as tk
from scores import Scores

class Window(tk.Tk, Scores):    
    def __init__(self):
        super().__init__()
        # All colors for the application
        self.window_color = "#121212"
        self.green = "#268321"
        self.white = "#F0F0F0"
        self.red = "#FF0000"
        self.light_gray = "#888888"
        self.yellow = "#ACB22D"
        self.incorrect = "#3D3D3D"
        self.column_background = "#565758"


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
            background=self.window_color,
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