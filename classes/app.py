if __name__ == "__main__":
    error_message = "Start this program with the \"start.py\" file"
    print(f"\033[1;31m{error_message}\033[0m")
    exit()
else:
    from lib.lib import *

class App(Keyboard, Board, EndScreen, Error):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.close) # When window gets closed

    def start(self):   
        self.mainloop()

    def close(self):
        self.add_player_game()
        self.destroy()

    def restart(self):
        self.enable_binding_events()
        self.new_board()
        self.new_keyboard()

    def game_over(self):
        self.disable_binding_events()
        self.disable_keyboard()
        self.add_player_game()
        self.end_screen()