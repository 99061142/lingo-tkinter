try:
    from classes.board import Board
    from classes.keyboard import Keyboard
    from classes.endScreen import endScreen
    from classes.error import Error
except ModuleNotFoundError:
    error_red = "\033[31m" + "This file is not meant to be run directly" + "\033[0m"
    print(error_red)
    exit()

class App(Keyboard, Board, endScreen, Error):
    def __init__(self):
        super().__init__()

    def start(self):   
        self.mainloop()

    def restart(self):
        self.enable_binding_events()
        self.new_board()
        self.new_keyboard()

    def game_over(self):
        self.disable_binding_events()
        self.disable_keyboard()
        self.add_player_game()
        self.end_screen()