import json
import sys


jsonInput = sys.argv[1]
s_json = jsonInput.lstrip()
decoder = json.JSONDecoder()
n = 0
s_lenth = len(s_json)
jsons = []

while len(s_json) > 0:
    data, n = decoder.raw_decode(s_json, 0)
    jsons.append(data)
    s_json = s_json[n:]
    s_json = s_json.lstrip()

json_count = len(jsons)
count_and_sequence = {"count": json_count, "seq.": jsons}
reverse_json_list = [json_count]

print(json.dumps(count_and_sequence), end=" ")
jsons.reverse()

for elem in jsons:
    reverse_json_list.append(elem)

print(json.dumps(reverse_json_list), end="")




