#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:45:48 2020

@author: andrewduffy
"""
import board
import tkinter as tk

# The value that is used to scale up the hexagon vertices into pixels. For example,
# If a vertex is at (1,0) it will instead be at (75,0).
TILE_SIZE = 75

# print the current board (i.e. the dictionary containing each tile) to the
# console. <USED FOR TESTING ONLY>
def simple_print(board):
    print(board.tiles())
    return 0

# Given an (x,y) corrdinate from a board grid, calculates the vertices scaled by the TILE_SIZE value (pixels)
# Input: an (x,y) coordinate
# Output: a list of vertices scaled by the TILE_SIZE value (pixels)
def get_hex_vertices(coordinate):
    size = TILE_SIZE
    points = [(size, 0), (2 * size, 0), (3 * size, size), (2 * size, 2 * size), (size, 2 * size), (0, size)]
    return [(x + (coordinate[0] * 2 * size) + 20, y + (coordinate[1] * size) + 20) for (x, y) in points]
  
# Given a list of vertices for a hexagon, finds the center
# Input: a list of integers representing a hexagon's vertices
# Output: A tuple containing the (x,y) coordinate in pixels of the hexagon's center
def find_center_of_tile(points):
    return ((points[2][0] + points[5][0]) / 2, (points[2][1] + points[5][1]) / 2)   

# Calculate a width and height that will fit the dimensions of the board using 
# the given dimensions and the TILE_SIZE variable
# Input: (number of columns, number of rows)
# Output: two integers representing a well-fitted width and height in pixels
def find_widthandheight(num_cols,num_rows):
    width = TILE_SIZE * ((num_cols * 4)+1) + 40
    height = TILE_SIZE * (num_rows+1) + 40
    return width,height

# Add a given tile's fish to the canvas. Currently represented by blue circles.
# Input: (tkinter canvas, a tile object, a list of this tile's vertices)
def add_fish_to_canvas(canvas,tile,points):
    center = find_center_of_tile(points)
    # generate a radius for the fish using the current tile's size
    radius = TILE_SIZE / 10
    offset = 3*radius
    curr_position = (center[0],center[1]-0.5*offset*(tile.num_fish-1))
    # for each fish, generate a circle a the intended location in the hexagon.
    for fish in range(0,tile.num_fish):
        oval_edges = [curr_position[0]-radius,curr_position[1]-radius,curr_position[0]+radius,curr_position[1]+radius]
        canvas.create_oval(oval_edges,fill="blue")
        #add an offset for the next fish
        curr_position = (curr_position[0],curr_position[1]+offset)

# Add a set of hexagonal tiles to a tkinter canvas
# Input: (tkinter canvas, dictionary with (x,y) coordinates as its keys and tile objects as its values)
# Output: Nothing, updates 'canvas'
def add_tiles_to_canvas(canvas,tiles):
    for key in tiles:
        tile = tiles[key]
        points = get_hex_vertices(key)
        canvas.create_polygon(points, outline='black', fill='red')
        add_fish_to_canvas(canvas,tile,points)

# Add all avatars for each player in 'players'. Currently shown as a circle
# Input: (tkinter canvas, list of player objects)
# Output: Nothing, updates 'canvas'
def add_avatars_to_canvas(canvas,players):
    for player in players:
        penguins = player.avatars
        for penguin in penguins:
            if penguin.position:
                points = get_hex_vertices(penguin.position)
                center = find_center_of_tile(points)
                radius = TILE_SIZE / 2
                offset = 3*radius
                curr_position = center
                oval_edges = [curr_position[0]-radius,curr_position[1]-radius,curr_position[0]+radius,curr_position[1]+radius]
                canvas.create_oval(oval_edges,fill=player.color)
        
    
# display the given board on a Tkinter canvas.
def tk_view(gamestate):
    board = gamestate.board
    players = gamestate.players
    tiles = board.tiles
    # Calculate the required GUI width and height from the tile size
    canvas_width,canvas_height = find_widthandheight(board.num_cols,board.num_rows)
    # Initialize a tkinter window and canvas with the specified canvas width
    # and height.
    window = tk.Tk()
    page = tk.Canvas(window, width=canvas_width, height=canvas_height)
    page.pack()
    # add tiles and avatars to the canvas
    add_tiles_to_canvas(page,tiles)
    add_avatars_to_canvas(page,players)
    # update the tkinter window
    window.mainloop()

