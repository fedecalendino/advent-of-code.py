def read(file: str) -> [list, list]:
    file = open(file)

    numbers = list(map(int, file.readline().split(",")))

    boards = []
    board = []

    for line in map(str.strip, file.readlines()):
        if not line:
            continue

        board.append(list(map(int, line.split())))

        if len(board) == 5:
            boards.append(board)
            board = []

    return numbers, boards
