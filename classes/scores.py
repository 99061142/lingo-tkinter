from classes.topHierachy import Type
import json

class Scores(metaclass=Type):
    _file = "storage/scores.json"

    def get_scores(self) -> list:
        with open(self._file, "r") as file:
            data = json.load(file)
        file.close()
        
        return data

    def get_games_played(self) -> int:
        return len(self.get_scores())

    def create_game_data(self) -> dict:
        data = {   
            "id": self.get_games_played(), 
            "word": self.word,
            "word_guesses": self.word_guesses,
            "won": self.word_guessed(),
            "tries": len(self.word_guesses),
        }
        return data

    def add_player_game(self):
        scores = self.get_scores()
        scores.append(self.create_game_data())
        
        with open(self._file, "w") as file:
            json.dump(scores, file, indent=4)
        file.close() 