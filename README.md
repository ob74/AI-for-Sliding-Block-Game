# AI-for-Sliding-Block-Game
Wrote Breadth First Search, Depth First Search and A Star (with Linear Conflict Heuristic) Algorithms to play a sliding block puzzle game

## Heuristic for A-Star

* Linear Conflict

    Is built on top of manhattan distance but it provides more optimal solutions because
    it checks if a piece is next to another piece which is not itself, 0 or -1(for the case where piece is 2)
    If this condition is met then there is a conflict, so the heuristic would adds a cost.

## Launching the program
Please call program with 3 arguments <filename in the same directory as this program> <Search Algorithm bfs, dfs, astar or id>
