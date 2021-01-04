import json
import sys
import nclib
import signal


TCP_PORT = sys.argv[1]
TCP_IP = '127.0.0.1'

if not TCP_PORT.isnumeric():
    print("Error: not postive int")
    print("usage: ./xgui positive-integer")
    quit()
else:
    TCP_PORT = int(TCP_PORT)

#https://docs.python.org/3/library/signal.html#example
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Connection took too long to respond")

signal.signal(signal.SIGALRM, handler)
signal.alarm(3)
try:
    nc = nclib.Netcat(listen=(TCP_IP, TCP_PORT))
except OSError:
    print("ERROR: connection took too long to respond")
    sys.exit(0)
signal.alarm(0)

s_json = nc.read()
s_json = str(s_json, 'utf-8')
s_json = s_json.lstrip()
decoder = json.JSONDecoder()
n = 0
# s_lenth = len(s_json)
jsons = []

while len(s_json) > 0:
    data, n = decoder.raw_decode(s_json, 0)
    jsons.append(data)
    s_json = s_json[n:]
    s_json = s_json.lstrip()

json_count = len(jsons)
count_and_sequence = {"count": json_count, "seq": jsons}
reverse_json_list = [json_count]

print(json.dumps(count_and_sequence), end=" ")
jsons.reverse()

for elem in jsons:
    reverse_json_list.append(elem)

print(json.dumps(reverse_json_list), end="")




