This document describes the protocol for a referee interacting with players and a tournament manager 
The protocol specifies what communication occurs in each phases of the game, from its creation to the its end. 
The protocol specifies four main phases for:
        
        •   Creating the game
        •   Placing all avatars
        •   Making turns / moving avatars
        •   Ending the game

Phase 1: Creating the Game
    
    •   CreateGame - The referee recieves a request from the tournament manager to create a game with a list of players. 
        This list of players is sorted in ascending order by age.
    •   The referee sets up a game of fish, setting up a state with a board, and determining how many penguins each player gets.
    •   SendGameState - The referee sends a copy of the new empty game state to each player
    •   AssignPlayer - The referee assigns each player a color, a turn order number, and an amount of penguins to be placed in the next
        round, then sends this information to each player
    
Phase 2: Placing Avatars

    
    •   SendGameState - The referee sends the current state to each player
    •   RequestPlacement - The referee sends a request to the next player who has a turn to place a penguin (starting with the youngest 
        player)
    •   PlaceAvatar - The referee waits to recieve a placement request from player. It then check the validity of the request
                        before updating the game state
    •   The referee updates the game state and detrmines whether the placemement phase is over. If the placement round is complete
            it begins the next phase of the game. If assignment is not over, it repeats the process with the next player who has a turn
        
Phase 3: Making turns / Moving Avatars

    •   StateUpdate - The referee sends the current state to all players
    •   RequestMove - The referee determines the next player who has a turn and sends them a request to make a move
    •   MoveAvatar - The player sends a request to move an avatar from its current y, x position, to a new y, x position.
                        The referee determines if the movement is valid, discards the move order and kicks the player if not
    •   The referee then updates the state with the valid movement, the determines if the game is over. If the game is over, the referee begins the next phase,
      but if the game is not over, it proceeds to the next turn and repeats the process
    • If a player does not respond within some timeout, then that player is assumed to be idle and is kicked.
      
        
Phase 4: Game Over

    •   NotifyGameOver - The referee determines the winner. It then sends a notification to each player containing 
        who won, who lost, and who cheated in the game.
    •   GameResults[PlayerInfo] - The referee informs the tournament manager of the game winner  
    
          Tournament Manager                                                                                     Player
                                                                joinTournament[Age, ID]
                  |   <------------------------------------------------------------------------------------------   |

                  |                                             Referee                                             |

                  |                                                |                                                |
                      CreateGame[PlayerInfo0, PlayerInfo1, ...]                                                        
                  |   ----------------------------------------->   |                                                |
                                                                            SendGameState[state, amtPenguins]                    
                  |                                                |   ----------------------------------------->   |
                                                                             AssignColor[color, penguinCount]        
                  |                                                |   ----------------------------------------->   |
                                                                  _____________________________________________________
                  |                                              |Until all penguins are placed |                   | |
                                                                 |______________________________|                     |
                  |                                              | |                                                | | 
                                                                 |                SendGameState                       | 
                  |                                              | |   ----------------------------------------->   | | 
                                                                 |                RequestPlacement                    | 
                  |                                              | |   ----------------------------------------->   | | 
                                                                 |                PlaceAvatar[x, y]                   | 
                  |                                              | |   <-----------------------------------------   | | 
                                                                 |____________________________________________________|
                  |                                                |                                                |
                                                                  ____________________________________________________
                  |                                              |Until no moves remain |                           | |
                                                                 |______________________|                             |
                  |                                              | |                                                | |
                                                                 |                SendGameState                       |
                  |                                              | |   ----------------------------------------->   | |
                                                                 |                 RequestMove                        |
                  |                                              | |   ----------------------------------------->   | |
                                                                 |      MoveAvatar[fromX, fromY, toX, toY]            |
                  |                                              | |   <-----------------------------------------   | |
                                                                 |____________________________________________________|
                  |                                                |                                                |
                                                                        NotifyGameOver[winners, losers, cheaters]      
                  |                                                |   ----------------------------------------->   |  
                        GameResults[winners, losers, cheaters]                  
                  |   <-----------------------------------------   |                                                |

