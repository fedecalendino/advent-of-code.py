class Pair:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f"{self.x}, {self.y}"


Position = Pair
Velocity = Pair


class Area:
    def __init__(self, x1: int, x2: int, y1: int, y2: int):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def is_in(self, position: Position):
        in_x = self.x1 <= position.x <= self.x2
        in_y = self.y2 >= position.y >= self.y1

        if in_x and in_y:
            return True

        passed_x = position.x > self.x2
        passed_y = position.y < self.y1

        if passed_x or passed_y:
            return None

        return False

    def __str__(self):
        return f"{self.x1}..{self.x2}, {self.y1}..{self.y2}"
