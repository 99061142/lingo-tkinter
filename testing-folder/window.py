from topHierachy import Type
import tkinter as tk

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
        # GUI keyboard characters / binding events for own keyboard
        self.keyboard_keys = [      
            {'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u' , 'i': 'i', 'o': 'o' , 'p': 'p'},
            {'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l'},
            {'Enter': '<Return>', 'z': 'z', 'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm', 'BackSpace': '<BackSpace>'}
        ]
        self.keyboard_chars = [char for row in self.keyboard_keys for char in row]
        self.binding_events = [row.get(char) for row in self.keyboard_keys for char in row]
        self.keyboard_buttons = {}

        self.window_config()
        self.enable_binding_events()

    def window_config(self):
        self.title("Wordle clone")
        self.geometry("1000x500")

        self.config(
            background=self._window_color,
        )

    def enable_binding_event(self, event:str):
        self.bind(event, lambda event=event: print(event))

        # Bind the uppercase character too
        if(len(event) == 1):
            self.bind(event.upper(), lambda event=event: print(event))

    def binding_event_to_char(self, event):
        
        return self.keyboard_chars[self.binding_events.index(event)]

    def enable_binding_events(self):
        for event in self.binding_events:
            char = self.binding_event_to_char(event).lower()
            self.bind(event, lambda event, char=char: print(char))

            # Bind the uppercase character too
            if(len(event) == 1):
                self.bind(event.upper(), lambda event, char=char: print(char))
    
    def disable_binding_event(self, event:str):
        self.unbind(event)

        # Unbind the uppercase character too
        if(len(event) == 1):
            self.unbind(event.upper())

    def disable_binding_events(self):
        for event in self.binding_events:
            self.unbind(event)

            # Unbind the uppercase character too
            if(len(event) == 1):
                self.unbind(event.upper())
