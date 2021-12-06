from _2019 import intcode


def part_01(file: str):
    program = intcode.from_file(file, 1)
    return program.run().output


def part_02(file: str):
    program = intcode.from_file(file, 5)
    return program.run().output


print("Part 01:", part_01("input.txt"))
print("Part 02:", part_02("input.txt"))
