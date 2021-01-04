#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:42:23 2020

@author: andrewduffy
"""

class Penguin:
    def __init__(self):
        self.position = None
        
    #Purpose: update the penguin's position to a given x,y coordinate
    # Signature: Position -> None
    def place(self, pos):
        self.position = pos
