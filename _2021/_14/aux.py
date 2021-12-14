def read(file: str):
    file = open(file)

    template: str = file.readline().strip()
    rules = []

    for line in file.readlines():
        line = line.strip()

        if not line:
            continue

        rules.append(tuple(line.split(" -> ")))

    return template, rules
