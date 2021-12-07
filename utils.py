from time import time


def read(file: str, mapper: callable = str) -> list:
    return list(
        map(
            lambda line: mapper(line),
            map(
                lambda line: line.strip(),
                open(file).readlines(),
            ),
        ),
    )


def read_chars(file: str, sep: str = ","):
    line = read(file)[0]

    if sep:
        return line.split(sep)

    return list(line)


def read_ints(file: str, sep: str = ","):
    return list(map(int, read(file)[0].split(sep)))


def timeit(method):
    def wrapper(*args, **kw):
        start = time()
        result = method(*args, **kw)
        end = time()

        total = end - start
        print(f"{method.__name__}  {total * 1000:.5f} ms.")

        return result

    return wrapper
