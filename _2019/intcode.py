import utils


class IntCode:
    ip: int = 0

    def __init__(self, memory: list[int], *input_: list):
        self.memory = memory
        self.input = input_ or []
        self.output = None

    def __getitem__(self, item):
        return self.memory[item]

    def __setitem__(self, key, value):
        self.memory[key] = value

    def __next__(self):
        instruction = self[self.ip]
        params, op = instruction // 100, instruction % 100
        params, mode_a = params // 10, params % 10
        params, mode_b = params // 10, params % 10

        match op:
            case 1:
                self.sum(mode_a, mode_b)
            case 2:
                self.mul(mode_a, mode_b)
            case 3:
                self.read()
            case 4:
                self.write(mode_a)
            case 5:
                self.jump_if_true(mode_a, mode_b)
            case 6:
                self.jump_if_false(mode_a, mode_b)
            case 7:
                self.less_than(mode_a, mode_b)
            case 8:
                self.equals(mode_a, mode_b)
            case 99:
                self.halt()
            case invalid:
                raise ValueError(f"{invalid} is not a valid opcode")

    def resolve(self, position: int, mode: int = 0):
        position = self.ip + position

        match mode:
            case 0:
                return self[self[position]]
            case 1:
                return self[position]
            case invalid:
                raise ValueError(f"{invalid} is not a valid parameter mode")

    # OPCODE: 1
    def sum(self, mode_a: int, mode_b: int):
        a = self.resolve(1, mode_a)
        b = self.resolve(2, mode_b)
        c = self.resolve(3, mode=1)

        self[c] = a + b

        self.ip += 4

    # OPCODE: 2
    def mul(self, mode_a: int, mode_b: int):
        a = self.resolve(1, mode_a)
        b = self.resolve(2, mode_b)
        c = self.resolve(3, mode=1)

        self[c] = a * b

        self.ip += 4

    # OPCODE: 3
    def read(self):
        a = self.resolve(1, mode=1)

        self[a], *self.input = self.input

        self.ip += 2

    # OPCODE: 4
    def write(self, mode_a: int):
        a = self.resolve(1, mode_a)

        self.output = a

        self.ip += 2

    # OPCODE: 5
    def jump_if_true(self, mode_a: int, mode_b: int):
        a = self.resolve(1, mode_a)
        b = self.resolve(2, mode_b)

        if a != 0:
            self.ip = b
        else:
            self.ip += 3

    # OPCODE: 6
    def jump_if_false(self, mode_a: int, mode_b: int):
        a = self.resolve(1, mode_a)
        b = self.resolve(2, mode_b)

        if a == 0:
            self.ip = b
        else:
            self.ip += 3

    # OPCODE: 7
    def less_than(self, mode_a: int, mode_b: int):
        a = self.resolve(1, mode_a)
        b = self.resolve(2, mode_b)
        c = self.resolve(3, mode=1)

        self[c] = 1 if a < b else 0

        self.ip += 4

    # OPCODE: 8
    def equals(self, mode_a: int, mode_b: int):
        a = self.resolve(1, mode_a)
        b = self.resolve(2, mode_b)
        c = self.resolve(3, mode=1)

        self[c] = 1 if a == b else 0

        self.ip += 4

    # OPCODE: 99
    def halt(self):
        raise StopIteration()

    def run(self):
        try:
            while True:
                next(self)
        except StopIteration:
            return self


def from_file(file: str, *input_) -> "IntCode":
    with open(file) as f:
        line = f.readline().strip()
        memory = list(map(int, line.split(",")))
        return IntCode(memory, *input_)


def test():
    assert from_file("_02/input.txt").run()[0] == 490699

    assert from_file("_05/input.txt", 1).run().output == 13818007
    assert from_file("_05/input.txt", 5).run().output == 3176266


if __name__ == "__main__":
    test()
