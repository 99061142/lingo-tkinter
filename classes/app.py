from classes.board import Board
from classes.keyboard import Keyboard
from classes.endScreen import endScreen
from classes.error import Error

class App(Keyboard, Board, endScreen, Error):
    def __init__(self):
        super().__init__()

    def start(self):   
        self.mainloop()

    def restart(self):
        self.new_board()
        self.enable_binding_events()
        self.new_keyboard()

    def game_over(self):
        self.disable_binding_events()
        self.disable_keyboard()
        self.add_player_game()
        self.end_screen()