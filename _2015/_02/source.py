import utils


def part_01(dimensions: list[tuple[int, int, int]]) -> int:
    def paper(box: tuple[int, int, int]) -> int:
        lenght, width, height = box
        sides = lenght * width, width * height, height * lenght

        return min(sides) + sum(map(lambda side: 2 * side, sides))

    return sum(map(paper, dimensions))


def part_02(dimensions: list[tuple[int, ...]]) -> int:
    def wrap(lenght: int, width: int, height: int) -> int:
        return min(
            [
                2 * lenght + 2 * width,
                2 * width + 2 * height,
                2 * height + 2 * lenght,
            ]
        )

    def bow(lenght: int, width: int, height: int) -> int:
        return lenght * width * height

    total = 0

    for box in dimensions:
        total += wrap(*box) + bow(*box)

    return total


def formatter(dimensions: str) -> tuple[int, ...]:
    return tuple(map(int, dimensions.split("x")))


input_values = utils.read("input.txt", formatter)

assert part_01([(2, 3, 4)]) == 58
assert part_01([(1, 1, 10)]) == 43
print("Part 01:", part_01(input_values))

assert part_02([(2, 3, 4)]) == 34
assert part_02([(1, 1, 10)]) == 14
print("Part 02:", part_02(input_values))
