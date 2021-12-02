import utils


def part_01(measures: list) -> int:
    return sum(
        map(
            lambda index: measures[index] > measures[index - 1],
            range(1, len(measures)),
        )
    )


def part_02(measures: list) -> int:
    return part_01(
        list(
            map(
                lambda index: sum(measures[index: index + 2]),
                range(len(measures) - 2),
            )
        )
    )


test_values = utils.read("test.txt", int)
input_values = utils.read("input.txt", int)

assert part_01(test_values) == 7
print("Part 01:", part_01(input_values))

assert part_02(test_values) == 5
print("Part 02:", part_02(input_values))
