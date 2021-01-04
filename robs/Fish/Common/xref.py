import sys
import json

sys.path.append('../')
sys.path.append('../Admin')

from referee import Referee

sys.path.append('../Player')

from player import Player

def handleJSON():
    jsonInput = sys.argv[1]
    s_json = jsonInput.lstrip()
    j = json.loads(s_json)

    num_row = j["row"]
    num_column = j["column"]
    player_info = j["players"]
    num_fish = j["fish"]
    players = []
    n = 0
    for info in player_info:
        players.append(Player(n, info[0], info[1]))
        n += 1

    return Referee(players, num_row, num_column, num_fish, randomize=False)


ref = handleJSON()

results = ref.play()
winners = results["winners"]
winners.sort()

sys.stdout.write(json.dumps(winners))

