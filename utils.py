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


def timeit(method):
    def wrapper(*args, **kw):
        start = time()
        result = method(*args, **kw)
        end = time()

        total = end - start
        print(f"{method.__name__}  {total * 1000:.5f} ms.")

        return result

    return wrapper
