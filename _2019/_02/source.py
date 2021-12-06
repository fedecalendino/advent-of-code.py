from _2019 import intcode


def part_01(file: str, noun: int = 12, verb: int = 2):
    program = intcode.from_file(file)
    program[1] = noun
    program[2] = verb

    return program.run()


def part_02(file: str):
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = part_01(file, noun, verb)

            if result == 19690720:
                return 100 * noun + verb


print("Part 01:", part_01("input.txt"))
print("Part 02:", part_02("input.txt"))
