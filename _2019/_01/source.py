from math import floor

import utils


def fuel(mass: int) -> int:
    return floor(mass / 3) - 2


def part_01(masses: list[int]) -> int:
    return sum(map(fuel, masses))


def part_02(masses: list[int]) -> int:
    if not masses:
        return 0

    fuel_requirements = list(
        filter(
            lambda fuel_needed: fuel_needed > 0,
            map(
                fuel,
                masses,
            ),
        )
    )

    return sum(fuel_requirements) + part_02(fuel_requirements)


input_values = utils.read("input.txt", int)

assert part_01([12]) == 2
assert part_01([14]) == 2
assert part_01([1969]) == 654
assert part_01([100756]) == 33583
print("Part 01:", part_01(input_values))

assert part_02([14]) == 2
assert part_02([1969]) == 966
assert part_02([100756]) == 50346
print("Part 02:", part_02(input_values))
