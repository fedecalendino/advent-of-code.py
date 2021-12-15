import heapq
import sys
from collections import defaultdict

import utils


def adjacents(x: int, y: int):
    return (
        (x - 1, y + 0),
        (x + 0, y - 1),
        (x + 0, y + 1),
        (x + 1, y + 0),
    )


def get(risk_levels: list[list[int]], tiles: int, x: int, y: int):
    d = len(risk_levels)

    if not -1 < x < d * tiles:
        return sys.maxsize

    if not -1 < y < d * tiles:
        return sys.maxsize

    x_tile_0 = x % d
    y_tile_0 = y % d

    x_bonus_per_tile = x // d
    y_bonus_per_tile = y // d

    risk = x_bonus_per_tile + y_bonus_per_tile + risk_levels[x_tile_0][y_tile_0]

    # Rounding
    if risk > 9:
        risk = risk - 9

    return risk


def dijkstra(risk_levels: list[list[int]], tiles: int) -> int:
    d = len(risk_levels)

    values = defaultdict(lambda: sys.maxsize)
    values[(0, 0)] = 0

    queue = []
    heapq.heappush(queue, (0, (0, 0)))

    visited = set()

    while queue:
        current_value, current = heapq.heappop(queue)

        if current in visited:
            continue

        for adjacent in adjacents(*current):
            adj_value = values[adjacent]
            adj_risk = get(risk_levels, tiles, *adjacent)

            if adj_value > current_value + adj_risk:
                adj_value = current_value + adj_risk
                values[adjacent] = adj_value
                heapq.heappush(queue, (adj_value, adjacent))

    return values[(tiles * d - 1, tiles * d - 1)]


def part_01(risk_levels: list[list[int]]):
    return dijkstra(risk_levels, tiles=1)


def part_02(risk_levels: list[list[int]]):
    return dijkstra(risk_levels, tiles=5)


def formatter(line: str):
    return list(map(int, line))


test_00_values = utils.read("test_00.txt", formatter)
test_01_values = utils.read("test_01.txt", formatter)
test_02_values = utils.read("test_02.txt", formatter)
input_values = utils.read("input.txt", formatter)

assert part_01(test_01_values) == 24
assert part_01(test_02_values) == 40
print("Part 01:", part_01(input_values))

assert part_02(test_02_values) == 315
print("Part 02:", part_02(input_values))
