from pathlib import Path

dir = Path().resolve()
input = Path(dir, "input/day2_input.txt")


class TestCase:
    def setup_class(cls):
        cls.input = """A X\nA X\nA Z\nB X\nA X"""
        cls.moves = ["A X", "A X", "A Z", "B X", "A X"]

    def test_input_is_read_correctly(self):
        """Rows are read correctly"""
        with open(input, "r") as f:
            all_moves: list[str] = f.readlines()
        # Remove the unnecessary whitespace, between the letters
        all_moves = [i.strip("\n").replace(" ", "") for i in all_moves]
        assert all_moves[0] == "AX"
        assert all_moves[3] == "BX"

    def test_create_player_and_enemy_arrays(self):
        """Separate rows into arrays for players"""
        expect_enemy = ["A", "A", "A", "B", "A"]
        expect_player = ["X", "X", "Z", "X", "X"]

        assert self.input.split("\n") == self.moves
        enemy = [i[0] for i in self.moves]
        player = [i[2] for i in self.moves]

        assert enemy == expect_enemy
        assert player == expect_player

    def test_convert_letters_to_points(self):
        """Convert the player/enemy moves into points, to total later."""
        enemy = ["A", "A", "A", "B", "A", "C", "C"]
        player = ["X", "X", "Z", "X", "X", "Z", "Y"]
        move_values = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
        enemy_points = [move_values[i] for i in enemy]
        player_points = [move_values[i] for i in player]

        assert enemy_points == [1, 1, 1, 2, 1, 3, 3]
        assert player_points == [1, 1, 3, 1, 1, 3, 2]

    def test_calculate_match_results(self):
        """Calculate each match's Win/Lose/Draw points for each player."""
        # 4 conditions in RPS are:
        # tie, rock > scissors, paper > rock, scissors > paper
        # 0 Lose, 3 Draw, 6 Win
        scores_chart = {
            # Draws ([e_score, p_score])
            "AX": [3, 3],
            "BY": [3, 3],
            "CZ": [3, 3],
            # R > S
            "AZ": [6, 0],
            "CX": [0, 6],
            # P > R
            "BX": [6, 0],
            "AY": [0, 6],
            # S > P
            "CY": [6, 0],
            "BZ": [0, 6],
        }

        moves = [i.replace(" ", "") for i in self.moves]
        scores = [scores_chart[i] for i in moves]

        assert scores == [[3, 3], [3, 3], [6, 0], [6, 0], [3, 3]]

    def test_player_totals_for_all_matches(self):
        """Calculate total sum of each player's match points."""
        scores = [[3, 3], [3, 3], [6, 0], [6, 0], [3, 3]]

        e_match_total = sum([i[0] for i in scores])
        p_match_total = sum([i[1] for i in scores])

        assert e_match_total == 21
        assert p_match_total == 9

    def test_player_total_scores_correct(self):
        """Calculate final total scores for both players."""
        enemy_move_points = [1, 1, 1, 2, 1]
        player_move_points = [1, 1, 3, 1, 1]
        scores = [[3, 3], [3, 3], [6, 0], [6, 0], [3, 3]]

        e_total = sum(enemy_move_points) + sum([i[0] for i in scores])
        p_total = sum(player_move_points) + sum([i[1] for i in scores])

        assert e_total == 27
        assert p_total == 16
