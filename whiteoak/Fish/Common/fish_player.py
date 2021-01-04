#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:18:13 2020

@author: andrewduffy
"""
import penguin


class FishPlayer:

    # A Player has:
    #   - Player ID
    #   - Age
    #   - Color
    #   - Avatars (Penguins)
    # Constructor takes in these fields and initializes the penguins
    def __init__(self,player_id,age,color,avatars = 0):
        self.player_id = player_id
        self.age = age
        self.color = color
        self.avatars = []
        for i in range(avatars):
            self.avatars.append(penguin.Penguin())

    # Returns JSON representation of player according to assignment:
    # Player is:
    #   Color
    #   Score
    #   Places (Piece Positions)
    # Takes in Score because Player should not store its own score
    # Signature: Score -> Dictionary
    def return_json(self, s):
        json_player = {"color": self.color, "score": s, "places": []}
        for avatar in self.avatars:
            if avatar.position:
                json_player["places"].append(convert_dw_to_pos(avatar.position))
            else:
                json_player["places"].append(None)
        return json_player


def convert_dw_to_pos(dwpos):
    new_x = 0
    if dwpos[1] % 2 == 0:
        new_x = dwpos[0] / 2
    else:
        new_x = (dwpos[0] - 1) / 2
    return (dwpos[1], int(new_x))