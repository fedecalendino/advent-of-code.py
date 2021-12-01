def read(file: str, cast: callable = str) -> list:
    return list(
        map(
            lambda line: cast(line),
            map(
                lambda line: line.strip(),
                open(file).readlines(),
            ),
        ),
    )
