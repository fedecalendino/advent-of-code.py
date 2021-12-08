import utils
from collections import defaultdict

ENCODING = {
    "ABCEFG": 0,
    "CF": 1,
    "ACDEG": 2,
    "ACDFG": 3,
    "BCDF": 4,
    "ABDFG": 5,
    "ABDEFG": 6,
    "ACF": 7,
    "ABCDEFG": 8,
    "ABCDFG": 9,
}


def get_possible_displays(patterns: list[str]) -> list[dict[str:str]]:
    by_len = defaultdict(list)

    for pattern in patterns:
        by_len[len(pattern)].append(pattern)

    possible_displays = [{}, {}, {}, {}, {}, {}, {}, {}]

    # Analyze ONE
    one = by_len[2][0]

    for index, display in enumerate(possible_displays):
        if index in [0, 2, 4, 6]:
            display["C"] = one[0]
            display["F"] = one[1]
        else:
            display["C"] = one[1]
            display["F"] = one[0]

    used_signals = set(one)

    # Analyze SEVEN
    seven = by_len[3][0]
    seven = [char for char in seven if char not in used_signals]

    for index, display in enumerate(possible_displays):
        display["A"] = seven[0]

    used_signals.update(seven)

    # Analyze FOUR
    four = by_len[4][0]
    four = [char for char in four if char not in used_signals]

    for index, display in enumerate(possible_displays):
        if index in [0, 1, 4, 5]:
            display["B"] = four[0]
            display["D"] = four[1]
        else:
            display["B"] = four[1]
            display["D"] = four[0]

    used_signals.update(four)

    # Analyze EIGHT
    eight = by_len[7][0]
    eight = [char for char in eight if char not in used_signals]

    for index, display in enumerate(possible_displays):
        if index in [0, 1, 2, 3]:
            display["E"] = eight[0]
            display["G"] = eight[1]
        else:
            display["E"] = eight[1]
            display["G"] = eight[0]

    return possible_displays


def to_digit(display: dict[str, str], signals: str):
    turned_on = "".join(
        filter(
            lambda segment: display[segment] in signals,
            "ABCDEFG",
        )
    )

    return ENCODING.get(turned_on)


def decode(patterns: list[str], digit_signals: list[str]) -> int:
    for display in get_possible_displays(patterns):
        digits = []

        for signals in digit_signals:
            digit = to_digit(display, signals)

            if digit is None:
                break

            digits.append(digit)

        if len(digits) == 4:
            return sum([v * (10 ** i) for i, v in enumerate(reversed(digits))])


def part_01(entries: list[tuple[list[str], list[str]]]) -> int:
    total = 0

    for patterns, signals in entries:
        found = str(decode(patterns, signals))

        total += found.count("1")
        total += found.count("4")
        total += found.count("7")
        total += found.count("8")

    return total


def part_02(entries: list[tuple[list[str], list[str]]]) -> int:
    total = 0

    for patterns, signals in entries:
        total += decode(patterns, signals)

    return total


def formatter(line: str) -> tuple[list[str], list[str]]:
    patterns, signals = line.split(" | ")
    return patterns.split(" "), signals.split(" ")


test_01_values = utils.read("test_01.txt", formatter)
test_02_values = utils.read("test_02.txt", formatter)
input_values = utils.read("input.txt", formatter)

assert part_01(test_01_values) == 0
assert part_01(test_02_values) == 26
print("Part 01:", part_01(input_values))

assert part_02(test_01_values) == 5353
assert part_02(test_02_values) == 61229
print("Part 02:", part_02(input_values))
