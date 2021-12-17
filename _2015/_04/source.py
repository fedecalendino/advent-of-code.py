from hashlib import md5


def solution(key: str, zeros: int):
    target = "0" * zeros

    i = 0

    while True:
        i += 1

        digest = md5(f"{key}{i}".encode("utf-8")).hexdigest()

        if digest[:zeros] == target:
            return i


assert solution("abcdef", zeros=5) == 609043
print("Part 01:", solution("yzbqklnj", zeros=5))

print("Part 02:", solution("yzbqklnj", zeros=6))
