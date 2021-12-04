import utils


def part_01(dimensions: list[tuple[int, ...]]) -> int:
    def calc(box: tuple[int, ...]) -> int:
        l, w, h = box
        sides = l * w, w * h, h * l

        return min(sides) + sum(map(lambda side: 2 * side, sides))

    return sum(map(calc, dimensions))


def formatter(dimensions: str) -> tuple[int, ...]:
    return tuple(map(int, dimensions.split("x")))


input_values = utils.read("input.txt", formatter)

assert part_01([[2, 3, 4]]) == 58
assert part_01([[1, 1, 10]]) == 43

print("Part 01:", part_01(input_values))
assert part_01(input_values) == 1586300
