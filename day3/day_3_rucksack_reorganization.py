from pathlib import Path

input: Path = Path("day3_input.txt")


def sum_common_items_priorities(input: Path) -> int:
    """Solve part 1."""
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


def sum_badge_type_priorities(input: Path) -> int:
    """Solve part 2."""
    with open(input) as f:
        lines: list[str] = f.read().splitlines()

    data: list[str] = [", ".join(lines[i : i + 3]) for i in range(0, len(lines), 3)]
    elves: list[list[str]] = [i.split(", ") for i in data]

    priorities: list[str] = []
    for i in elves:
        common: str = "".join(set(i[0]).intersection(i[1], i[2]))
        priorities.append(common)

    print(priorities[0:5])
    priority_values: list[int] = [
        ord(char) - 96 if char == char.lower() else ord(char) - 38
        for char in priorities
    ]
    print(sum(priority_values))
    return sum(priority_values)


if __name__ == "main":
    sum_common_items_priorities(input)
    sum_badge_type_priorities(input)
