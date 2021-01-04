#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:44:13 2020

@author: andrewduffy, miraisahara
"""

import sys
import Tkinter as tk

if len(sys.argv) > 2:
    print("usage: ./xgui single-positive-integer")
    sys.exit(2)

try:
    size = int(sys.argv[1])
except:
    print("usage: ./xgui positive-integer")
    sys.exit(2)

if size <= 0:
    print("usage: ./xgui positive-integer")
    sys.exit(2)

points = [size, 0, 2 * size, 0, 3 * size, size, 2 * size, 2 * size, size, 2 * size, 0, size]

for ii, point in enumerate(points):
    points[ii] = points[ii] + 0

window = tk.Tk()

page = tk.Canvas(window, width=(size * 3) + 20, height=(2 * size) + 20)

page.create_polygon(points, outline='red', fill='', tags='hexagon')

page.place(relx='0.5', rely='0.5', anchor=tk.CENTER)


def endit(event):
    event.widget.master.destroy()


page.tag_bind('hexagon', "<Button-1>", endit)

page.pack()

window.mainloop()
