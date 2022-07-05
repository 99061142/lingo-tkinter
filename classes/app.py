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


    def previous_label_config(self):
        # Set the styling of the rows that were already guessed
        for row, word in enumerate(self.word_guesses):
            self.check_characters(word, row)

    def start(self):    
        if self.previous_game_over() == False:
            self.previous_label_config()
        self.mainloop()
        

    def close(self):
        self.destroy()
        self.add_player_game()

    def restart(self):
        self.enable_binding_events()
        self.new_board()
        self.new_keyboard()

    def game_over(self):
        self.disable_binding_events()
        self.disable_keyboard()
        self.add_player_game()
        self.end_screen()