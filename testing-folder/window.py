from topHierachy import Type

class Window(metaclass=Type):
    # All colors for the application
    _window_color = "#121212"
    _green = "#268321"
    _white = "#F0F0F0"
    _red = "#FF0000"
    _light_gray = "#888888"
    _key_incorrect_position = "#ACB22D"
    _key_incorrect = "#3D3D3D"
    
    def __init__(self):
        print("WINDOW")