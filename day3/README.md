# Day 3 - Rucksack Reorganization

## Part 1
Each rucksack has 2 Lg COMPARTMENTS

- All items of given type are meant to go into exactly one of the two
- Elf failed to follow this rule for exactly one item tytpe per rucksack

**Problem:** Find item type that appears in both compartments of each rucksack.
Calculate  sum of the priorities of those item types

### Puzzle Input

- All the item currently each rucksack
  -  Item types are single, case-sensitive letters (i.e. a & A refer to
      different item types)
- Items per rucksack is given as chas all on a single line
- Given rucksack always has the same num of items in both compartments
  - First half of chars represent items in first compart, 2nd half items
    in 2nd compartment

**Sample Input:**
  - Row 1:
    - vJrwpWtwJgWrhcsFMMfFFhFp
    - C1: vJrwpWtwJgWr
    - C2: hcsFMMfFFhFp
    - Item in both: p (priority 16)
  - Row 2:
    - jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    - C1: rsFMfFZSrLrFZsSL
    - C2: rsFMfFZSrLrFZsSL
    - Common item: L (priority 38)
  - Row 3: P
  - Row 4: v
  - Row 5: t
  - Row 6: s
Item types can be convnerted to a priority
  - a-z: 1-26
  - A-Z: 27-52


## Exercise Two

Elves in groups of 3.
Each elf carries a badge (which is only common `item type` amongst the 3 elves)

**Problem:** Find common item type between all 3 elves in each group, then sum the priorities

### Sample Input

Group 1:

- vJrwpWtwJgWrhcsFMMfFFhFp
  - jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
  - PmmdzqPrVvPwwTWBwg
  - Common Type: r
  - Priority: 18

Group 2:
  - wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
  - ttgJtRGJQctTZtZT
  - CrZsJsPPZsGzwwsLwLmpwMDw
  - Common: Z
  - Priority: 52
