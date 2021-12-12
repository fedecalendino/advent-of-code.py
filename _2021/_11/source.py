from itertools import count

import utils


def get(octopuses: list[list[int]], x: int, y: int):
    if not -1 < x < len(octopuses):
        return None

    if not -1 < y < len(octopuses[x]):
        return None

    return octopuses[x][y]


def adjacents(x: int, y: int):
    return (
        (x - 1, y - 1),
        (x - 1, y + 0),
        (x - 1, y + 1),
        (x + 0, y - 1),
        (x + 0, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 0),
        (x + 1, y + 1),
    )


def flash(octopuses, x, y) -> int:
    octopus = get(octopuses, x, y)

    if octopus in [None, 0]:
        return 0

    if octopus < 9:
        octopuses[x][y] += 1
        return 0

    octopuses[x][y] = 0

    return 1 + sum(
        map(
            lambda adjacent: flash(octopuses, *adjacent),
            adjacents(x, y),
        )
    )


def step(octopuses: list[list[int]]) -> int:
    flashes = 0
    to_flash = set()

    for i in range(len(octopuses)):
        for j in range(len(octopuses)):
            octopuses[i][j] += 1

            if octopuses[i][j] > 9:
                to_flash.add((i, j))

    for i, j in to_flash:
        flashes += flash(octopuses, i, j)

    return flashes


def part_01(octopuses: list[list[int]]) -> int:
    return sum(
        map(
            lambda _: step(octopuses),
            range(0, 100),
        )
    )


def part_02(octopuses: list[list[int]]) -> int:
    for n in count(1):
        if step(octopuses) == 100:
            return n


def formatter(line: str):
    return list(map(int, line))


test_values = utils.read("test.txt", formatter)
input_values = utils.read("input.txt", formatter)

assert part_01(test_values) == 1656
print("Part 01:", part_01(input_values))


test_values = utils.read("test.txt", formatter)
input_values = utils.read("input.txt", formatter)

assert part_02(test_values) == 195
print("Part 02:", part_02(input_values))
