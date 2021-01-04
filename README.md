# CS4500 - Software Development

Developed a game of "Fish" from scratch. It's a relatively simple game played on a hexagonal grid where penguins move to collect fish for points.

The scope of this project went:
- Internal game logic. Representing the board and other components, calculating possible moves, player scores, turn order, etc.
- Game States and Trees. Any point in a game can be represented in a State. A tree can be created to represent an entire game where each node has a State and each edge represents some player's move.
- Referees that can run entire games and return the results (winners, losers, detected cheaters or AFK players).
- Tournament Managers that can run entire tournaments by taking in signups and grouping players into games and running those games in rounds until winner(s) emerge.
- Allowing remote players by adapting local code using a proxy pattern.
- Implementing remote players over actual network connections (incomplete in this final codebase). 

Course structure was as follows:
- Work with first partner for majority of semester
- Switch to a new partner (in my case I was onboarded to a new codebase)
- Switch to a final partner (in my case I onboarded this new partner)
- Present third/final codebase to professor

whiteoak - The first codebase. All code in here is me and my first partner's (pair programmed). 

robs - The codebase I onboarded onto. Majority of the code here is not written by me. Worked on 2 assignments with new partner on this codebase.

athens - The final codebase. This is the same as robs, but worked on with a new partner. Worked on 1 final assignment before final code walks.
