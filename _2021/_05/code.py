import utils
from math import atan2, degrees
from collections import defaultdict


def angle(x1: int, y1: int, x2: int, y2: int):
    return degrees(atan2(y2 - y1, x2 - x1))


def draw_line(grid: dict[tuple[int, int], int], x1: int, y1: int, x2: int, y2: int):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x, y] += 1


def draw_diagonal(grid: dict[tuple[int, int], int], x1: int, y1: int, x2: int, y2: int):
    xd = 1 if x1 < x2 else -1
    yd = 1 if y1 < y2 else -1

    x, y = x1, y1

    while x != x2 + xd and y != y2 + yd:
        grid[x, y] += 1

        x, y = x + xd, y + yd


def solution(segments: list, diagonals: bool = False) -> int:
    grid = defaultdict(lambda: 0)

    for segment in segments:
        match abs(angle(*segment)):
            case 0.0 | 90.0 | 180.0:
                draw_line(grid, *segment)
            case 45.0 | 135.0:
                diagonals and draw_diagonal(grid, *segment)

    return sum(
        map(
            lambda value: value >= 2,
            grid.values()
        )
    )


def formatter(line: str) -> tuple[int, int, int, int]:
    start, end = line.split(" -> ")
    x1, y1 = tuple(start.split(","))
    x2, y2 = tuple(end.split(","))

    return int(x1), int(y1), int(x2), int(y2)


test_values = utils.read("test.txt", formatter)
input_values = utils.read("input.txt", formatter)

assert solution(test_values) == 5
assert solution(input_values) == 6564
print("Part 01:", solution(input_values))

assert solution(test_values, diagonals=True) == 12
assert solution(input_values, diagonals=True) == 19172
print("Part 02:", solution(input_values, diagonals=True))

