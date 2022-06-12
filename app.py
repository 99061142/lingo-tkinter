from board import Board
from keyboard import Keyboard
from endScreen import endScreen
from error import Error

class App(Keyboard, Board, endScreen, Error):
    def __init__(self):
        super().__init__()

    def start(self):
        self.mainloop()

    def restart(self):
        self.new_game()
        self.enable_binding_events()
        self.enable_keyboard()

    def game_over(self):
        self.disable_binding_events()
        self.disable_keyboard()
        self.save_game_data()
        self.end_screen()

    def save_game_data(self):  
        guessed_correctly = self.word_guesses[-1] == self._word
        tries = self.round if (guessed_correctly) else self.round - 1

        # Add the game info
        game = {   
            "game_id": self.get_games_played() + 1, 
            "correct_word": self._word,
            "all_word_guesses": self.word_guesses,
            "guessed_correctly": guessed_correctly,
            "tries": tries,
        }
        self.add_player_game(game)




if __name__ == "__main__":
    app = App()
    app.start()