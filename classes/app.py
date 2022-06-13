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
        self.save_game_data()
        self.end_screen()

    def save_game_data(self):  
        guessed_correctly = self.word_guesses[-1] == self.word
        tries = len(self.word_guesses)

        # Add the game info
        game = {   
            "id": self.get_games_played(), 
            "word": self.word,
            "word_guesses": self.word_guesses,
            "won": guessed_correctly,
            "tries": tries,
        }
        self.add_player_game(game)