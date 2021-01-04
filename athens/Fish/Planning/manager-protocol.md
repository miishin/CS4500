This document describes the protocol for a tournament manager and a referee
communicating with each other. The protocol specifies what communication
occurs in certain phases of the game. 
The protocol specifies three main phases for:
        
        •   Creating referees
        •   Play a round
        •   Evaluate tourniment


    
Phase 1: creating referees
    
    •   getPlayers - a tournament manager would run this method in order to get the players for a game of fish from the queue of weighting players
    •   ageSort[playerList] - this will sort the list of players by there age parameter
    •   createRef - Creates the referees which will then create the game. 
                    This takes in a list of players and the amount of rows and columns in a board
    
    
Phase 2: play a round

    •   runTournement[State] - this method starts the first round of the game and asks for the state
    •   getRoundResults[ref] - runs getResults on the referees of each game in the round and sets up the next round if applicable
    

Phase 3: evaluate tournament round

    •   getresults - runs getResults on the referees of each game in the round and sets up the next round if applicable
    •   This creates a new queue which contains only the winners
    •   If the tournament is not over, starts again  at phase 1 with the winners queue
    •   If the tournament is over, informs players about the results
    




    Tournement manager                              referee
                                                     
      _____________________________________________________
     |creating referees             |                   | |
     |______________________________|                     |
     | |                                                | | 
     |      createRef[players, amtRow, amtCol]            | 
     | |   ----------------------------------------->   | | 
     |____________________________________________________|
       |                                                |
      ____________________________________________________
     |play a round          |                           | |
     |______________________|                             |
     | |                                                | |
     |                runTournement[State]                |
     | |   ----------------------------------------->   | |
     |               getRoundResults[ref]                 |
     | |   ----------------------------------------->   | |
     |____________________________________________________|
       |                                                |
                        getResults[ref]      
       |   ----------------------------------------->   |                                                 |

                                                         








