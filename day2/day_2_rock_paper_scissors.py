from pathlib import Path

input = Path("day2/day2_input.txt")

# Note: the exercise only requires the player's score.
# I thought it made sense to calculate the enemy's score as well.


def calculate_rps_player_score(input: Path) -> int:
    """Calculate player & enemy scores, and return player score."""
    move_values: dict[str, int] = {
        # Value of choices for Rock, Paper, Scissors
        "A": 1,
        "X": 1,
        "B": 2,
        "Y": 2,
        "C": 3,
        "Z": 3,
    }

    scores_chart: dict[str, list[int]] = {
        # "Moves": [player_score, enemy_score]
        # Draw
        "AX": [3, 3],
        "BY": [3, 3],
        "CZ": [3, 3],
        # Rock > Scissors
        "AZ": [6, 0],
        "CX": [0, 6],
        # Paper > Rock
        "BX": [6, 0],
        "AY": [0, 6],
        # Scissors > Paper
        "CY": [6, 0],
        "BZ": [0, 6],
    }

    with open(input, "r") as f:
        all_moves: list[str] = f.readlines()
    # Remove the unnecessary whitespace, between the letters
    all_moves = [i.strip("\n").replace(" ", "") for i in all_moves]

    # Create array of selected moves for each player
    enemy: list[str] = [i[0] for i in all_moves]
    player: list[str] = [i[1] for i in all_moves]

    # Calculate total points from the moves selected in each match
    enemy_move_points: list[int] = [move_values[i] for i in enemy]
    player_move_points: list[int] = [move_values[i] for i in player]

    # Create list of [enemy score, player score] lists for each match
    match_scores: list[list[int]] = [scores_chart[i] for i in all_moves]

    # Total = Move Points + Match Scores
    enemy_total: int = sum(enemy_move_points) + sum([i[0] for i in match_scores])
    player_total: int = sum(player_move_points) + sum([i[1] for i in match_scores])

    print("Emeny Total: ", enemy_total)
    print("Player Total: ", player_total)
    return player_total


if __name__ == "main":
    calculate_rps_player_score(input)
