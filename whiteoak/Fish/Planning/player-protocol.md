Communication to and from a referee should take a JSON format so that any referee adhering to this standard can be subbed in.

get_current_game - the player should be able to get the current GameState

    {
        "command": "get_game"
    }
    
The Referee responds with a JSON representation of a GameState:
    
    {
        "players": Player*,
        "board": Board
    }
    
a Player is:
    
    {
        "color": Color,
        "score": Natural,
        "places": [Position, ..., Position]
    }
    
A Board is a 2d JSON array
    
    [
        [x1, x2, x3, ...]
        [y1, y2, y3, ...]
        ...
    ]
    where each number in array = num of fish on tile with 0 denoting a hole
    
place - players place avatars to start the game

    {
        "command": "place",
        "location": [x, y]
    }
    
The Referee responds with whether that placement was legal (if it was legal it should have been placed)

    true
    or
    false
    
move - if the player wants to move a piece from (x1,y1) to (x2,y2) then the referee will need to take that and validate the movement:

    {
        "command": "move",
        "movement": [[x1, y1], [x2, y2]]
    }

The Referee responds with whether the move was legal (legal move should be executed):

    true
    or
    false
    
get_score - the player should be able to query to get their score (this isn't saved in a player object):

    {
        "command": "get_score"
    }
    
The Referee responds with the player's score:

    Score
    
get_children - the player should be able to query the next children from the current game state in the tree

    {
        "command": "get_children"
    }
    
expand_node - the player should be able to query the next node in the tree given a move from the current node

    {
        "command": "expand_node"
        "move": [[x1, y1], [x2, y2]]
    }