if __name__ == "__main__":
    error_message = "Start this program with the \"start.py\" file"
    print(f"\033[1;31m{error_message}\033[0m")
    exit()
else:
    from lib.lib import *

class Scores(metaclass=Type):
    _file = "storage/scores.json"

    def create_file(self):
        # Create the scores file if it wasn't created yet
        with open(self._file, 'w') as file:
            json.dump([], file, indent=4)
        file.close()

    def get_games(self) -> list:
        # If the scores file doesn't exists
        if not os.path.exists(self._file):
            self.create_file()  

        with open(self._file, "r") as file:
            data = json.load(file)
        file.close()

        return data

    def get_games_played(self) -> int:
        return len(self.get_games())

    def create_game_data(self) -> dict:
        data = {   
            "id": self.get_games_played(), 
            "word": self.word,
            "word_guesses": self.word_guesses,
            "won": self.word_guessed(),
            "game_over": self.game_is_over(),
            "tries": len(self.word_guesses)
        }
        return data

    def add_player_game(self):
        scores = self.get_games()
        scores.append(self.create_game_data())
        
        with open(self._file, "w") as file:
            json.dump(
                scores, 
                file, 
                indent=4
            )
        file.close() 


    def previous_game(self):
        return self.get_games()[-1] if self.get_games() else None

    def previous_word(self):
        return self.previous_game()['word'] if self.previous_game() else None

    def previous_game_over(self):
        return self.previous_game()['game_over'] if self.previous_game() else None

    def previous_word_guessed(self):
        return self.previous_game()['word_guesses'] if self.previous_game() else None
    
    def previous_round(self):
        return self.previous_game()['tries'] if self.previous_game() else None

    def game_is_over(self):
        try:
            return self.state() == "normal" # If the game is over when the window is open
        except: 
            return len(self.word_guesses) == 5 # Check if the user has guesses left when the user left midgame