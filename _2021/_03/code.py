from functools import reduce
import utils


def bin2dec(digits) -> int:
    return int("".join(map(str, digits)), 2)


def most_common_values(diagnostic_report: list):
    half = len(diagnostic_report) / 2

    def transform(value: int):
        if value > half:
            return 1

        if value < half:
            return 0

        return None

    return tuple(
        map(
            transform,
            tuple(
                reduce(  # sum all values into one
                    lambda a, b: tuple(map(sum, zip(a, b))),
                    diagnostic_report,
                ),
            ),
        )
    )


def find_rating(report: list, keep_value: int, index: int = 0):
    if len(report) == 1:
        return bin2dec(report[0])

    mcv = most_common_values(report)[index]

    tmp = []

    for item in report:
        if mcv is None:
            if item[index] == keep_value:
                tmp.append(item)
        elif (item[index] == mcv) == keep_value:
            tmp.append(item)

    return find_rating(tmp, keep_value, index + 1)


def part_01(diagnostic_report: list) -> int:
    mcv = most_common_values(diagnostic_report)

    gamma = bin2dec(mcv)
    epsilon = bin2dec(map(lambda value: int(not value), mcv))

    return gamma * epsilon


def part_02(diagnostic_report: list) -> int:
    oxygen_generator_rating = find_rating(diagnostic_report, keep_value=1)
    co2_scrubber_rating = find_rating(diagnostic_report, keep_value=0)

    return oxygen_generator_rating * co2_scrubber_rating


def formatter(line: str):
    return list(map(int, line))


test_values = utils.read("test.txt", formatter)
input_values = utils.read("input.txt", formatter)


assert part_01(test_values) == 198
assert part_01(input_values) == 3959450
print("Part 01:", part_01(input_values))

assert part_02(test_values) == 230
assert part_02(input_values) == 7440311
print("Part 02:", part_02(input_values))
