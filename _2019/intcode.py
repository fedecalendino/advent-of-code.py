import utils


class IntCode:
    def __init__(self, memory: list[int]):
        self.memory = memory
        self.ip = 0

    def __getitem__(self, item):
        return self.memory[item]

    def __setitem__(self, key, value):
        self.memory[key] = value

    def __next__(self):
        op = self[self.ip]

        match op:
            case 1:
                self.sum()
            case 2:
                self.mul()
            case 99:
                self.halt()
            case invalid:
                raise ValueError(f"{invalid} is not a valid opcode")

    # OPCODE: 1
    def sum(self):
        ip = self.ip

        source_a, source_b, target = self[ip + 1: ip + 4]
        self[target] = self[source_a] + self[source_b]

        self.ip += 4

    # OPCODE: 2
    def mul(self):
        ip = self.ip

        source_a, source_b, target = self[ip + 1: ip + 4]
        self[target] = self[source_a] * self[source_b]

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


def from_file(file: str) -> "IntCode":
    with open(file) as f:
        line = f.readline().strip()
        memory = list(map(int, line.split(",")))
        return IntCode(memory)


def test():
    assert from_file("_02/input.txt").run()[0] == 490699


if __name__ == "__main__":
    test()
