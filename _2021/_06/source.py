import utils


def solution(fishes: list[int], days: int):
    timers = [0] * 10

    for fish in fishes:
        timers[fish] += 1

    for _ in range(days):
        snapshot = [0] * 10

        for days_left in range(0, 9):
            if days_left == 0:
                snapshot[6] += timers[0]
                snapshot[8] += timers[0]
            else:
                snapshot[days_left - 1] += timers[days_left]

        timers = snapshot

    return sum(timers)


def formatter(line: str) -> list[int]:
    return list(map(int, line.split(",")))


test_values = utils.read_ints("test.txt")
input_values = utils.read_ints("input.txt")

assert solution(test_values, days=18) == 26
assert solution(test_values, days=80) == 5934

print("Part 01:", solution(input_values, days=80))
print("Part 02:", solution(input_values, days=256))
