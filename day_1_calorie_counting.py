from pathlib import Path

input_file: Path = Path("input/day1_input.txt")


def find_largest_calories(input: Path) -> int:
    with open(input, "r") as f:
        # Create a list containing a string with the values
        # for each elf, based on the newlines in the input file.
        # Each list is a single string, with numbers broken up by newlines
        data = f.read().split("\n\n")

    # (Move code outside read loop, so we don't waste memory)
    # Convert the single strings into normal lists, with
    # calorie numbers for each elf). Elf rows now look like:
    # ['3120', '4127', '1830', '1283', '5021', '3569', '3164', '2396', '4367', '2821', '6118', '4450', '1300', '3648', '1933']
    data = [i.splitlines() for i in data]

    # Convert the strings into integers, via a double-list comprehension.
    # The inner comprehension does the conversion.
    # The outer comprehension replaces the previous table rows.
    # Elf rows now look like:
    # [3120, 4127, 1830, 1283, 5021, 3569, 3164, 2396, 4367, 2821, 6118, 4450, 1300, 3648, 1933]
    data = [[int(i) for i in row] for row in data]

    # Sum up the values in each elf's row
    data = [sum(i) for i in data]

    # Sort totals in ascending order. print(data[-3:]) shows
    # the last 3 values are: [66855, 68056, 68292]
    data = sorted(data)

    # Return the final item in the list (which is our highest total)
    print(data[len(data) - 1])
    return data[len(data) - 1]


find_largest_calories(input_file)
