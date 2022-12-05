from pathlib import Path

input: Path = Path("input/day3_input.txt")

# Each rucksack has 2 Lg COMPARTMENTS
#     # All items of given type are meant to go into exactly one of the two
#     # Elf failed to follow this rule for exactly one item tytpe per rucksack

# Puzzle input:
#   All the items currently each rucksack
#     #  Item types are single, case-sensitive letters (i.e. a & A refer to
#          different item types)
# Items per rucksack is given as chas all on a single line
# Given rucksack always has the same num of items in both compartments
#     # First halff of chars represent items in first compart, 2nd half items
#       in 2nd compartment
# Sample Input:
#     # vJrwpWtwJgWrhcsFMMfFFhFp
#         # C1: vJrwpWtwJgWr
#         # C2: hcsFMMfFFhFp
#         # Item in both: p (priority 16)
#     # jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#         # C1: rsFMfFZSrLrFZsSL
#         # C2: rsFMfFZSrLrFZsSL
#         # Common item: L (priority 38)
#     # Row 3: P
#     # Row 4: v
#     # Row 5: t
#     # Row 6: s
# Item types can be convnerted to a priority
#     # a-z: 1-26
#     # A-Z: 27-52
# Find item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types
#
# The whole thing about "2 compartments" was completely irrelevant... you just need to find the letter that shows up twice


def sum_common_items_priorities(self) -> int:
    with open(input) as f:
        lines: list[str] = f.read().splitlines()

    common_chars: list[str] = []

    for sack in lines:
        comp1: str = sack[: len(sack) // 2]
        comp2: str = sack[len(sack) // 2 : len(sack)]
        unique: str = "".join(set(comp1).intersection(comp2))
        common_chars.append(unique)

    common_int_values = [
        ord(char) - 96 if char == char.lower() else ord(char) - 38
        for char in common_chars
    ]

    print(sum(common_int_values))
    return sum(common_int_values)


sum_common_items_priorities(input)
