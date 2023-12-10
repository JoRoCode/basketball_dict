import db

class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]
        

    def player_info(self,players):
        player_list = []
        for player in range(0, len(players,[])):
            player_list.append(db(players)["name"])
            return player_list
        
        
print(player_kevin)