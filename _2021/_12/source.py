import utils
from collections import defaultdict


def make_graph(rules: list[tuple[str, str]]) -> dict[str, list[str]]:
    graph = defaultdict(list)

    for start, end in rules:
        graph[start].append(end)

        if start != "start" and end != "end":
            graph[end].append(start)

    return graph


def find_paths_01(
    graph: dict[str, list[str]], current: str, visited: list = None
) -> list[list[str]]:
    visited = visited or []

    if current == "end":
        return [["end"]]

    if current in visited:
        return []

    if current.islower():
        visited.append(current)

    paths = []
    path = [current]

    for cave in graph[current]:
        for found in find_paths_01(graph, cave, list(visited)):
            paths.append(path + found)

    return paths


def part_01(rules: list[tuple[str, str]]) -> int:
    graph = make_graph(rules)
    found = find_paths_01(graph, "start")

    return len(found)


def find_paths_02(
    graph: dict[str, list[str]], current: str, visited: list = None
) -> list[list[str]]:
    visited = visited or []

    if current == "end":
        return [["end"]]

    if current in visited:
        if current == "start":
            return []

        if "flag" in visited:
            return []

        visited.append("flag")

    if current.islower():
        visited.append(current)

    paths = []
    path = [current]

    for cave in graph[current]:
        for found in find_paths_02(graph, cave, list(visited)):
            paths.append(path + found)

    return paths


def part_02(rules: list[tuple[str, str]]) -> int:
    graph = make_graph(rules)
    found = find_paths_02(graph, "start")

    return len(found)


def formatter(line: str) -> tuple:
    return tuple(line.split("-"))


test_01_values = utils.read("test_01.txt", formatter)
test_02_values = utils.read("test_02.txt", formatter)
test_03_values = utils.read("test_03.txt", formatter)
input_values = utils.read("input.txt", formatter)

assert part_01(test_01_values) == 10
assert part_01(test_02_values) == 19
assert part_01(test_03_values) == 226
print("Part 01:", part_01(input_values))


assert part_02(test_01_values) == 36
assert part_02(test_02_values) == 103
assert part_02(test_03_values) == 3509
print("Part 02:", part_02(input_values))
