from collections import defaultdict, Counter

from aux import read


def step(polymer: dict[str, int], rules: dict[str, str]) -> dict[str, int]:
    new = defaultdict(int)

    for pair, count in polymer.items():
        if pair in rules:
            first_pair, second_pair = rules[pair]

            new[first_pair] += count
            new[second_pair] += count
        else:
            new[pair] += count

    return new


def solution(template: str, rules: list[tuple[str, str]], steps: int) -> int:
    polymer = Counter(map(lambda i: template[i : i + 2], range(len(template) - 1)))
    rules = {pair: [pair[0] + element, element + pair[1]] for pair, element in rules}

    for _ in range(steps):
        polymer = step(polymer, rules)

    counter = defaultdict(int)

    for pair, count in polymer.items():
        counter[pair[0]] += count

    counter[template[-1]] += 1

    return max(counter.values()) - min(counter.values())


test_values = read("test.txt")
input_values = read("input.txt")

assert solution(*test_values, steps=10) == 1588
print("Part 01:", solution(*input_values, steps=10))

assert solution(*test_values, steps=40) == 2188189693529
print("Part 02:", solution(*input_values, steps=40))
