#!/usr/bin/env python3

# A player component that uses the code in Common to actually play Fish

class Player:

    # A Player is initialized with a strategy component that it will use to make decisions
    def __init__(self, player_id, strategy):
        self.player_id = player_id
        self.strategy = strategy

    # Chooses an action for the turn
    # Signature: GameState Integer -> Move
    def choose_action(self, gamestate, depth):
        return self.strategy.choose_action(gamestate, depth)

    # Chooses a placement for the turn
    # Signature: GameState -> Position
    def place_penguin(self, gamestate):
        return self.strategy.place_penguin(gamestate)

