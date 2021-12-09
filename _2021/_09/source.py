import utils
from functools import reduce


def get(heightmap: list[list[int]], x: int, y: int):
    if not -1 < x < len(heightmap):
        return 9

    if not -1 < y < len(heightmap[x]):
        return 9

    return heightmap[x][y]


def adjacents(heightmap: list[list[int]], x: int, y: int):
    return (
        get(heightmap, x - 1, y),
        get(heightmap, x + 1, y),
        get(heightmap, x, y - 1),
        get(heightmap, x, y + 1),
    )


def risk(heightmap: list[list[int]], x: int, y: int):
    value = get(heightmap, x, y)
    return (0, value + 1)[value < min(adjacents(heightmap, x, y))]


def basin(heightmap: list[list[int]], points: set, x: int, y: int):
    value = get(heightmap, x, y)

    if value == 9:
        return

    points.add((x, y))

    for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if (i, j) in points:
            continue

        basin(heightmap, points, i, j)


def part_01(heightmap: list[list[int]]):
    risk_level = 0

    for i, row in enumerate(heightmap):
        for j, _ in enumerate(row):
            risk_level += risk(heightmap, i, j)

    return risk_level


def part_02(heightmap: list[list[int]]):
    basins = []

    for i, row in enumerate(heightmap):
        for j, _ in enumerate(row):
            if not risk(heightmap, i, j):
                continue

            points = set()
            basin(heightmap, points, i, j)
            basins.append(len(points))

    return reduce(
        lambda a, b: a * b,
        sorted(basins, reverse=True)[:3],
    )


def formatter(line: str):
    return list(map(int, line))


test_values = utils.read("test.txt", formatter)
input_values = utils.read("input.txt", formatter)

assert part_01(test_values) == 15
print("Part 01:", part_01(input_values))

assert part_02(test_values) == 1134
print("Part 02:", part_02(input_values))
