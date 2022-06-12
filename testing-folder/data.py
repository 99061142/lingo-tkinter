from topHierachy import Type
import json

class Data(metaclass=Type):
    def get_player_games(self) -> int:
        with open("scores.json", "r") as file:
            data = json.load(file)
        file.close()

        return len(data)

    def add_player_game(self, game:dict):
        print(game)

        with open("scores.json", "r") as file:
            data = json.load(file)
        file.close()

        data.append(game)

        with open("scores.json", "w") as file:
            json.dump(data, file)