import utils

from collections import defaultdict


def deliver(directions: list[str]) -> dict[tuple[int, int]]:
    houses = defaultdict(int)
    houses[(0, 0)] = 1

    x, y = 0, 0

    for direction in directions:
        match direction:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1

        houses[(x, y)] += 1

    return houses


def part_01(directions: list[str]) -> int:
    return len(deliver(directions))


def part_02(directions: list[str]) -> int:
    santa = []
    robo = []

    for index, direction in enumerate(directions):
        if index % 2:
            santa.append(direction)
        else:
            robo.append(direction)

    return len((deliver(santa) | deliver(robo)))


test_01_values = utils.read_chars("test_01.txt", sep="")
test_02_values = utils.read_chars("test_02.txt", sep="")
input_values = utils.read_chars("input.txt", sep="")

assert part_01(test_01_values) == 4
assert part_01(test_02_values) == 2
print("Part 01:", part_01(input_values))

assert part_02(test_01_values) == 3
assert part_02(test_02_values) == 11
print("Part 02:", part_02(input_values))