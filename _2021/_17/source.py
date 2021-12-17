import sys

from classes import Area, Position, Velocity


def step(position: Position, velocity: Velocity):
    position.x += velocity.x
    position.y += velocity.y

    if velocity.x > 0:
        velocity.x -= 1
    elif velocity.x < 0:
        velocity.x += 1

    velocity.y -= 1


def test(velocity: Velocity, target_area: Area) -> int:
    position = Position(0, 0)
    max_y = -sys.maxsize

    while True:
        step(position, velocity)

        is_probe_in = target_area.is_in(position)

        if is_probe_in is True:
            return max_y

        if is_probe_in is None:
            return None

        max_y = max(max_y, position.y)


def part_01(x1: int, x2: int, y1: int, y2: int) -> int:
    trench = Area(x1, x2, y1, y2)

    highest_y = -sys.maxsize

    for x in range(1, 100):
        for y in range(-100, 100):
            velocity = Velocity(x, y)
            best_y = test(velocity, trench)

            if best_y is None:
                continue

            highest_y = max(best_y, highest_y)

    return highest_y


def part_02(x1: int, x2: int, y1: int, y2: int) -> int:
    trench = Area(x1, x2, y1, y2)

    velocities = 0

    for x in range(1, 275):
        for y in range(-275, 275):
            velocity = Velocity(x, y)

            best_y = test(velocity, trench)

            if best_y is None:
                continue

            velocities += 1

    return velocities


test_values = (20, 30, -10, -5)
input_values = (192, 251, -89, -59)

assert part_01(*test_values) == 45
print("Part 01:", part_01(*input_values))

assert part_02(*test_values) == 112
print("Part 02:", part_02(*input_values))
