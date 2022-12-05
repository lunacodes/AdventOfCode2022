from pathlib import Path

# dir = Path().resolve()
input: Path = Path("day3/day3_input.txt")


class TestCase:
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
