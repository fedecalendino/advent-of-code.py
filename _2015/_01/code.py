import utils


def part_01(directions: str) -> int:
    floor = 0

    for direction in directions:
        match direction:
            case "(":
                floor += 1
            case ")":
                floor -= 1

    return floor


def part_02(directions: str) -> int:
    floor = 0

    for index, direction in enumerate(directions, start=1):
        match direction:
            case "(":
                floor += 1
            case ")":
                floor -= 1

        if floor == -1:
            return index

    return 0


input_values = utils.read("input.txt")[0]

assert part_01("(())") == 0
assert part_01("(()(()(") == 3
assert part_01("))(((((") == 3
assert part_01(")())())") == -3

assert part_01(input_values) == 232
print("Part 01:", part_01(input_values))

assert part_02(")") == 1
assert part_02("()())") == 5

assert part_02(input_values) == 1783
print("Part 02:", part_02(input_values))
