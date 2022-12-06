from pathlib import Path

dir = Path().resolve()
input: Path = Path("day3/day3_input.txt")


class TestSumCommonItemPriorities:
    def test_file_read(self):
        with open(input) as f:
            lines: list[str] = f.read().splitlines()

        assert lines[0] == "RCMRQjLLWGTjnlnZwwnZJRZH"
        assert lines[(len(lines) - 1)] == "bGFnGljgSsjBCTBszz"

    def test_split_string_into_compartments(self):
        """Determine that we split each list item into the correct 2 compartments"""

        sack: str = "vJrwpWtwJgWrhcsFMMfFFhFp"
        compartment_1: str = "vJrwpWtwJgWr"
        compartment_2: str = "hcsFMMfFFhFp"
        assert sack[: len(sack) // 2] == compartment_1
        assert sack[len(sack) // 2 : len(sack)] == compartment_2

    def test_find_common_char(self):
        # For exercise 1
        compartment_1: str = "vJrwpWtwJgWr"
        compartment_2: str = "hcsFMMfFFhFp"
        common_chars = "".join(set(compartment_1).intersection(compartment_2))

        # TODO: Add additional test inputs
        assert common_chars == "p"

    def test_convert_letters_to_ints(self):
        item_types = "pLPvts"

        # Ord starts at 97. lowercase letters are -96. Uppercase are minus 38
        nums = [
            (ord(char) - 96) if char == char.lower() else ord(char) - 38
            for char in item_types
        ]

        assert nums == [16, 38, 42, 22, 20, 19]


class TestSumBadgeTypePriorities:
    def test_split_into_groups_of_three(self):
        data_in = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
        # Convert to list (imitating f.readlines())
        data = data_in.split("\n")

        # list items contain a string with 3 comma-separated values
        new_data = [", ".join(data[i : i + 3]) for i in range(0, len(data), 3)]

        # Convert strings into a list item with 3 values
        new_data = [i.split(", ") for i in new_data]

        assert new_data[0] == [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ]

    def test_find_common_chars(self):
        line1: str = "vJrwpWtwJgWrhcsFMMfFFhFp"
        line2: str = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
        line3: str = "PmmdzqPrVvPwwTWBwg"

        common_chars = "".join(set(line1).intersection(line2, line3))
        assert common_chars == "r"
