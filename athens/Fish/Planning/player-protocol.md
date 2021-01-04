This document describes the protocol for a player and referee 
communicating with each other. The protocol specifies what communication
occurs in certain phases of the game. 
The protocol specifies four main phases for:
        
        •   Creating the game
        •   Placing all avatars
        •   Making turns / moving avatars
        •   Ending the game

Phase 1: Creating the Game
    
    •   joinGame() - A player uses the joinGame method to send a message with their age and id 
        to a referee to get them into a new game.
    •   The referee creates a game once it has enough join requests to create a game
    •   SendGameState - The referee sends a copy of the new empty game state to each player
    •   AssignPlayer - The referee assigns each player a color, a turn order number, and an amount of penguins to be placed in the next
        round, then sends this information to the player
    
Phase 2: Placing Avatars

    
    •   SendGameState - The referee sends the current state to all players
    •   RequestPlacement - The referee sends a request to the next player who has a turn to place a penguin (starting with the youngest 
        player)
    •   PlaceAvatar - The player sends their placement to the referee
    •   The referee updates the game state and detrmines whether the placemement phase is over, assigns the next turn to
        the next youngest player and repeats the process
        
Phase 3: Making turns / Moving Avatars

    •   StateUpdate - The referee sends the current state to all players
    •   RequestMove - The referee determines the next player who has a turn and sends them a request to make a move
    •   Move - The player sends a move of an avatar from its current y, x position, to a new y, x position
    •   The referee then updates the state, the determines if the game is over, and moves to the next turn if not
  
Phase 4: Game Over

    •   NotifyGameOver - The referee determines the winner. It then sends a notification to each player containing 
        who won, who lost, and who cheated in the game.
    




    Referee                                          Player
                       joinGame[Age, ID]                 
       |   <-----------------------------------------   |
                        SendGameState                    
       |   ----------------------------------------->   |
                 AssignColor[color, penguinCount]        
       |   ----------------------------------------->   |
      _____________________________________________________
     |Until all penguins are placed |                   | |
     |______________________________|                     |
     | |                                                | | 
     |                SendGameState                       | 
     | |   ----------------------------------------->   | | 
     |                RequestPlacement                    | 
     | |   ----------------------------------------->   | | 
     |                PlaceAvatar[x, y]                   | 
     | |   <-----------------------------------------   | | 
     |____________________________________________________|
       |                                                |
      ____________________________________________________
     |Until no moves remain |                           | |
     |______________________|                             |
     | |                                                | |
     |                SendGameState                       |
     | |   ----------------------------------------->   | |
     |                 RequestMove                        |
     | |   ----------------------------------------->   | |
     |         MoveAvatar[fromX, fromY, toX, toY]         |
     | |   <-----------------------------------------   | |
     |____________________________________________________|
       |                                                |
            NotifyGameOver[winners, losers, cheaters]      
       |   ----------------------------------------->   |  
                                                         

