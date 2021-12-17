import utils


def part_01(strings: list[str]) -> int:
    def is_nice(string: str) -> bool:
        if any(filter(lambda word: word in string, ["ab", "cd", "pq", "xy"])):
            return False

        if len(list(filter(lambda char: char in "aeiou", string))) < 3:
            return False

        if any(
            map(lambda char: f"{char}{char}" in string, "abcdefghijklmnopqrstuvwxyz")
        ):
            return True

        return False

    return len(list(filter(is_nice, strings)))


def part_02(strings: list[str]) -> int:
    def is_nice(string: str) -> bool:
        for index in range(len(string) - 2):
            first = string[index]
            second = string[index + 2]

            if first == second:
                break
        else:
            return False

        for index in range(len(string) - 2):
            first = string[index]
            second = string[index + 1]

            if f"{first}{second}" in string[index + 2:]:
                break
        else:
            return False

        return True

    return len(list(filter(is_nice, strings)))


input_values = utils.read("input.txt")

assert part_01(["ugknbfddgicrmopn"]) == 1
assert part_01(["aaa"]) == 1
assert part_01(["jchzalrnumimnmhp"]) == 0
assert part_01(["haegwjzuvuyypxyu"]) == 0
assert part_01(["dvszwmarrgswjxmb"]) == 0
print("Part 01:", part_01(input_values))

assert part_02(["qjhvhtzxzqqjkmpb"]) == 1
assert part_02(["xxyxx"]) == 1
assert part_02(["uurcxstgmygtbstg"]) == 0
assert part_02(["ieodomkazucvgmuy"]) == 0
print("Part 02:", part_02(input_values))
