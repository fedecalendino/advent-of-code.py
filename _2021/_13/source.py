import utils


def show(dots: set[tuple[int, int]]):
    max_x = max(map(lambda xy: xy[0], dots))
    max_y = max(map(lambda xy: xy[1], dots))

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            print(("▫️️", "⬛️")[(x, y) in dots], end="")
        print()


def fold(dots: set[tuple[int, int]], folds: list[tuple, str, int]) -> set[tuple[int, int]]:
    for coordinate, value in folds:
        new = set()

        for x, y in dots:
            match coordinate:
                case "y":
                    if x > value:
                        x = abs(value - abs(value - x))
                case "x":
                    if y > value:
                        y = abs(value - abs(value - y))

            new.add((x, y))

        dots = new

    return dots


def part_01(dots: set[tuple[int, int]], folds: list[tuple, str, int]) -> int:
    return len(fold(dots, folds[:1]))


def part_02(dots: set[tuple[int, int]], folds: list[tuple, str, int]) -> set[tuple[int, int]]:
    return fold(dots, folds)


def read(file: str):
    dots = set()
    folds = list()

    for line in utils.read(file):
        if not line:
            continue

        if line.startswith("fold along"):
            coordinate, value = line.replace("fold along ", "").split("=")
            folds.append((coordinate, int(value)))
        else:
            x, y = line.split(",")
            dots.add((int(y), int(x)))

    return dots, folds


test_values = read("test.txt")
input_values = read("input.txt")

assert part_01(*test_values)
print("Part 01:", part_01(*input_values))

print("Part 02:")
result = part_02(*input_values)
show(result)


# Result: (HKUJGAJZ)
"""
⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️▫️️▫️️⬛️⬛️▫️️▫️️⬛️⬛️▫️️▫️️▫️️⬛️⬛️▫️️▫️️▫️️▫️️⬛️⬛️▫️️⬛️⬛️⬛️⬛️
⬛️▫️️▫️️⬛️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️▫️️⬛️▫️️▫️️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️▫️️▫️️▫️️⬛️▫️️▫️️▫️️▫️️⬛️
⬛️⬛️⬛️⬛️▫️️⬛️⬛️▫️️▫️️▫️️⬛️▫️️▫️️⬛️▫️️▫️️▫️️▫️️⬛️▫️️⬛️▫️️▫️️▫️️▫️️⬛️▫️️▫️️⬛️▫️️▫️️▫️️▫️️⬛️▫️️▫️️▫️️⬛️▫️️
⬛️▫️️▫️️⬛️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️▫️️⬛️▫️️▫️️▫️️▫️️⬛️▫️️⬛️▫️️⬛️⬛️▫️️⬛️⬛️⬛️⬛️▫️️▫️️▫️️▫️️⬛️▫️️▫️️⬛️▫️️▫️️
⬛️▫️️▫️️⬛️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️▫️️
⬛️▫️️▫️️⬛️▫️️⬛️▫️️▫️️⬛️▫️️▫️️⬛️⬛️▫️️▫️️▫️️⬛️⬛️▫️️▫️️▫️️⬛️⬛️⬛️▫️️⬛️▫️️▫️️⬛️▫️️▫️️⬛️⬛️▫️️▫️️⬛️⬛️⬛️⬛️
"""