import utils


def read(file: str):
    dots = set()
    folds = list()

    for line in utils.read(file):
        if not line:
            continue

        if line.startswith("fold along"):
            coordinate, value = line.replace("fold along ", "").split("=")
            folds.append((coordinate, int(value)))
        else:
            x, y = line.split(",")
            dots.add((int(y), int(x)))

    return dots, folds
