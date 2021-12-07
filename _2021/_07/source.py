import utils
from statistics import median, mean


def part_01(crabs: list[int]) -> int:
    def fuel(target: int, positions: list[int]) -> int:
        return sum(
            map(
                lambda p: abs(target - p),
                positions,
            )
        )

    position = median(crabs)  # sorted(crabs)[len(crabs) // 2]
    return int(fuel(position, crabs))


def part_02(crabs: list[int]) -> int:
    def fuel(target: int, positions: list[int]) -> int:
        return sum(
            map(
                lambda n: n * (n + 1) // 2,  # 1 + 2 + 3 + ... + n
                map(
                    lambda p: abs(target - p),
                    positions,
                ),
            ),
        )

    position = int(mean(crabs))  # sum(crabs) // len(crabs)
    return min(fuel(position, crabs), fuel(position + 1, crabs))


test_values = utils.read_ints("test.txt")
input_values = utils.read_ints("input.txt")

assert part_01(test_values) == 37
print("Part 01:", part_01(input_values))

assert part_02(test_values) == 168
print("Part 02:", part_02(input_values))
