#!/usr/bin/env python
import sys

cmd = ""
x = 0
lenOfPrompts = len(sys.argv)
if lenOfPrompts > 1:
    if sys.argv[1] == "-limit":
        if lenOfPrompts == 2:
            while x < 20:
                print("hello world")
                x = x + 1
        else:
            del sys.argv[0:2]
            for word in sys.argv:
                if cmd == "":
                    cmd = word
                else:
                    cmd = cmd + " " + word

            while x < 20:
                print(cmd)
                x = x + 1
    else:
        del sys.argv[0]
        for word in sys.argv:
            if cmd == "":
                cmd = word
            else:
                cmd = cmd + " " + word
        while True:
            print(cmd)
else:
    while True:
        print("hello world")
