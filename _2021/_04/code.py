import aux
import utils
from collections import defaultdict


def check_row(boards: list, board: int, row: int) -> bool:
    return sum(boards[board][row]) == -5


def check_column(boards: list, board: int, column: int) -> bool:
    return sum(map(lambda row: row[column], boards[board])) == -5


def check(boards: list, board: int, row: int, column: int) -> bool:
    return check_row(boards, board, row) or check_column(boards, board, column)


def mark(boards: list, board: int, row: int, column: int):
    boards[board][row][column] = -1


# Helps finding the places of each number in each board quicker.
def make_values_index(boards: list) -> dict[int, [list[tuple[int]]]]:
    values = defaultdict(list)

    for board_index, board in enumerate(boards):
        for row_index, row in enumerate(board):
            for column_index, value in enumerate(row):
                values[value].append((board_index, row_index, column_index))

    return values


def find_winners(numbers: list, boards: list) -> tuple[list[int], list[int]]:
    values = make_values_index(boards)

    winning_boards = []
    winning_numbers = []

    for number in numbers:
        if len(winning_boards) == len(boards):
            break

        for board_index, row_index, column_index in values.get(number, []):
            if board_index in winning_boards:
                continue

            mark(boards, board_index, row_index, column_index)

            if check(boards, board_index, row_index, column_index):
                winning_boards.append(board_index)
                winning_numbers.append(number)

    return winning_numbers, winning_boards


def sum_board(boards: list, board: int) -> int:
    total = 0

    for row in boards[board]:
        for value in row:
            total += (0, value)[value > 0]

    return total


@utils.timeit
def solution(numbers: list, boards: list) -> tuple[int, int]:
    winning_numbers, winning_boards = find_winners(numbers, boards)

    part_01_solution = winning_numbers[0] * sum_board(boards, winning_boards[0])
    part_02_solution = winning_numbers[-1] * sum_board(boards, winning_boards[-1])

    return part_01_solution, part_02_solution


part_01, part_02 = solution(*aux.read("test.txt"))
assert part_01 == 4512
assert part_02 == 1924

part_01, part_02 = solution(*aux.read("input.txt"))
assert part_01 == 16716
assert part_02 == 4880

part_01, part_02 = solution(*aux.read("input.txt"))
print("Part 01:", part_01)
print("Part 02:", part_02)
