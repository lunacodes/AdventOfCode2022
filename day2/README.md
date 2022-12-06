## Day 2 - Rock Paper Scissors

**Problem:** Calculate total player score

total_score = sum(scores_per_match)
score_per_match = player_move + outcome
  Moves:    1 Rock, 2 Paper, 3 Scissors
  Outcomes: 0 Lose, 3 Draw, 6 Win

**Sample Data** (each line is an RPS match):
Enemy          | Player          | Enemy Score | Player Score | Winner
A (Rock 1)     | Y (Paper 2)     |  1 (1, 0)   |  8 (2, 6)    | Player
B (Paper 2)    | X (Rock 1)      |  8 (2, 6)   |  1 (1, 0)    | Enemy
C (Scissors 3) | Z (Scissiors 3) |  6          | 6            | Draw

Player Total: 15
Enemy Total: 15
