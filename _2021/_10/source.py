import utils

from typing import Union


PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


CORRUPTED_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_SCORES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def analyze(line: str) -> Union[str, list]:
    stack = []

    for char in line:
        if char in "([{<":
            stack.append(char)
            continue

        expected = PAIRS.get(char)

        if stack[-1] != expected:
            return char

        stack.pop()

    return stack


def part_01(lines: list[str]) -> int:
    def score(result: str):
        return CORRUPTED_SCORES[result]

    return sum(
        map(
            score,
            filter(
                lambda result: isinstance(result, str),
                map(
                    analyze,
                    lines,
                ),
            ),
        )
    )


def part_02(lines: list[str]) -> int:
    def score(result: list):
        tmp = 0

        for char in reversed(result):
            tmp = tmp * 5 + INCOMPLETE_SCORES[char]

        return tmp

    scores = sorted(
        map(
            score,
            filter(
                lambda result: isinstance(result, list),
                map(
                    analyze,
                    lines,
                ),
            ),
        )
    )

    return scores[len(scores) // 2]


test_values = utils.read("test.txt")
input_values = utils.read("input.txt")

assert part_01(test_values) == 26397
print("Part 01:", part_01(input_values))

assert part_02(test_values) == 288957
print("Part 02:", part_02(input_values))
