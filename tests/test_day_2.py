from pathlib import Path

input = Path("../input/day_2_input.txt")


class TestCase:
    def setup_class(cls):
        cls.input = """A X\nA X\nA Z\nB X\nA X"""
        cls.moves = ["A X", "A X", "A Z", "B X", "A X"]

    def test_input_is_read_correctly(self):
        """Rows are read correctly"""
        with open(input, "r") as f:
            while True:
                line1 = f.readline()
                line2 = f.readline()
                if not line2:
                    break

        assert line1 == "A X"
        assert line2 == "A X"

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
        enemy = ["A", "A", "A", "B", "A", "C", "C"]
        player = ["X", "X", "Z", "X", "X", "Z", "Y"]
        move_values = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
        enemy_points = [move_values[i] for i in enemy]
        player_points = [move_values[i] for i in player]

        assert enemy_points == [1, 1, 1, 2, 1, 3, 3]
        assert player_points == [1, 1, 3, 1, 1, 3, 2]

    def test_calculate_round_winner(self):
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
            "ZB": [0, 6],
        }

        moves = [i.replace(" ", "") for i in self.moves]
        scores = [scores_chart[i] for i in moves]

        assert scores == [[3, 3], [3, 3], [6, 0], [6, 0], [3, 3]]

    def test_player_totals_per_round(self):
        enemy_move_points = [1, 1, 1, 2, 1]
        player_move_points = [1, 1, 3, 1, 1]
        scores = [[3, 3], [3, 3], [6, 0], [6, 0], [3, 3]]

        e_total = sum(enemy_move_points) + sum([i[0] for i in scores])
        p_total = sum(player_move_points) + sum([i[1] for i in scores])

        assert sum(enemy_move_points) == 6
        assert sum([i[0] for i in scores]) == 21
        assert e_total == 27
        assert sum(player_move_points) == 7
        assert sum([i[1] for i in scores]) == 9
        assert p_total == 16
