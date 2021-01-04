#!/usr/bin/env python3

# Setting up tournament

# Open up for requests to join tournament
# Signature: None -> None
def open_for_join():
    ...

# Organizing players into games
# Signature: Listof(Player) -> Listof(Game)
def organize_players():
    ...

# Sets up games with a referee
# Signature: Listof(Game) -> None
def assign_referee():
    ...

# Organizes the games into a given format
# Signature: Format -> None
def organize_games(format):
    ...

# Tells referees to run their games
# Signature: None -> None
def run_games():
    ...

# Receive game results from referees
# Signature: Referee -> Results
def receive_results(referee):
    ...

# Check if the next round of games can be started
# Signature: None -> Boolean
def can_start_next_round():
    ...

# Check if there is a tournament winner
# Signature: None -> Boolean
def is_tournament_over():
    ...

# Open up for Observer requests
# Signature: None -> None
def get_observer_requests():
    ...

# Parse observer requests and respond
# Signature: Request -> None
def respond_to_observer(request):
    ...

# Returns tournament rankings
# Signature: None -> Rankings
def get_rankings():
    ...

# Returns view of a requested game
# Signature: GameID -> Image
def view_game(g_id):
    ...


