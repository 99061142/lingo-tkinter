from topHierachy import Type
import json

class Scores(metaclass=Type):
    def get_scores(self) -> list:
        with open("scores.json", "r") as file:
            data = json.load(file)
        file.close()
        
        return data

    def get_games_played(self) -> int:
        return len(self.get_scores())

    def add_player_game(self, game:dict):
        scores = self.get_scores()
        scores.append(game)
        
        with open("scores.json", "w") as file:
            json.dump(scores, file)
        file.close() 