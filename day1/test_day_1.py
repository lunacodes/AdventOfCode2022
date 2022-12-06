from pathlib import Path

input: Path = Path("day1/input.txt")


class TestClass:
    def test_line_count(self):
        with open(input, "r") as file:
            calorie_list = file.readlines()
        assert len(calorie_list) == 2237

    def test_numbers_are_added_as_ints(self):
        with open(input, "r") as file:
            cal_list = [int(x) for x in file.read().split()]
        assert cal_list[0] == 3120

    def test_blank_line_found_correctly(self):
        mock_list_str = """
        3120
        4127
        1830
        1283
        5021
        3569
        3164
        2396
        4367
        2821
        6118
        4450
        1300
        3648
        1933

        4841
        6135
        """

    def test_list_sorted_in_ascending_order(self):
        mock_list = [300, 20, 50, 75]
        mock_list.sort()

        assert mock_list[0] == 20
        assert mock_list[-1] == 300
