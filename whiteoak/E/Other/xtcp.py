#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:27:08 2020

@author: andrewduffy
"""
#%% Imports
import sys
import socket as s
import jsonparse as js
import xjson

#%% Set the port and hostname for the server
in_port = 4567
in_hostname = s.gethostname()
timeout = 3

numargs = len(sys.argv)
# check if the program was given a non-default port
# and whether there is only one argument
if numargs == 2:
    try:
        in_port = int(sys.argv[1])
    except:
        print("invalid port")
        sys.exit(2)
elif numargs > 2:
    print("usage: ./xtcp port-number")
    sys.exit(2)

# Quick check if it's a valid TCP port
if in_port < 1024 or in_port > 65535:
    print("Port number should be in range 1024-65535")
    sys.exit(2)

#%% Open a socket and set it's default values
try:
    server = s.socket()
    server.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
    server.settimeout(timeout)
    server.bind((in_hostname,in_port))
    server.listen(1)
except Exception as e:
    print("Error creating server.")
    print(e)
    server.close()
    sys.exit(1)

#%% Wait for a client communication, loop after com. is received
json = ""
try:
    cl, address = server.accept()
except:
    print("No client connection detected.")
    sys.exit(1)
cl.setblocking(False)
cl.settimeout(timeout)

while 1:
    try: 
        rec = cl.recv(4096)
        rec = rec.decode()
        if rec == '':
            break
        json+= rec    
    except:  
        break

 
#%% Wrap up the receive-side 
server.close()   

#%% Convert the input json values to the output
try:
    json_values = js.read_json_string(json)
    output_json = xjson.formFullResponse(json_values)
except:
    print("Bad JSON")

#%% Send the JSON output to client
cl.sendall(output_json.encode())
cl.close()