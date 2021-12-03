import utils


def part_01(commands: list) -> int:
    depth, horizontal = 0, 0

    for command, value in commands:
        match command:
            case "forward":
                horizontal += value
            case "down":
                depth += value
            case "up":
                depth -= value
            case unknown:
                raise ValueError(f"{unknown} is a valid command")

    return horizontal * depth


def part_02(commands: list) -> int:
    aim, depth, horizontal = 0, 0, 0

    for command, value in commands:
        match command:
            case "forward":
                horizontal += value
                depth += aim * value
            case "down":
                aim += value
            case "up":
                aim -= value
            case unknown:
                raise ValueError(f"{unknown} is a valid command")

    return horizontal * depth


def formatter(command: str):
    direction, value = command.split()
    return direction, int(value)


test_values = utils.read("test.txt", formatter)
input_values = utils.read("input.txt", formatter)

assert part_01(test_values) == 150
assert part_01(input_values) == 1746616
print("Part 01:", part_01(input_values))

assert part_02(test_values) == 900
assert part_02(input_values) == 1741971043
print("Part 02:", part_02(input_values))
