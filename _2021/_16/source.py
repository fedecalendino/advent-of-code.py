import utils
from aux import bin_to_dec, hex_to_bin

from functools import reduce


OPERATIONS = {
    0: (
        "sum",
        lambda values: reduce(
            lambda x, y: x + y,
            values,
        ),
    ),
    1: (
        "mul",
        lambda values: reduce(
            lambda x, y: x * y,
            values,
        ),
    ),
    2: (
        "min",
        lambda values: reduce(
            min,
            values,
        ),
    ),
    3: (
        "max",
        lambda values: reduce(
            max,
            values,
        ),
    ),
    5: (
        "gt",
        lambda values: reduce(
            lambda x, y: int(x > y),
            values,
        ),
    ),
    6: (
        "lt",
        lambda values: reduce(
            lambda x, y: int(x < y),
            values,
        ),
    ),
    7: (
        "eq",
        lambda values: reduce(
            lambda x, y: int(x == y),
            values,
        ),
    ),
}


def parse_literal_packet(bits: list[int]):
    group = 1
    digits = []

    while group:
        group, bits = bits[0], bits[1:]
        value, bits = bits[:4], bits[4:]

        digits.extend(value)

    return bin_to_dec(digits), bits


def parse_operator_packet(bits: list[int], packet_type_id: int):
    version_sum = 0

    length_type_id, bits = bits[0], bits[1:]

    if length_type_id:
        count, bits = bin_to_dec(bits[:11]), bits[11:]

        values = []

        for _ in range(count):
            version, value, bits = parse_packet(bits)

            values.append(value)
            version_sum += version
    else:
        length, bits = bin_to_dec(bits[:15]), bits[15:]
        subpackets, bits = bits[:length], bits[length:]

        version, values, _ = parse_packets(subpackets)
        version_sum += version

    op_name, op_func = OPERATIONS[packet_type_id]

    result = op_func(values)

    return version_sum, result, bits


def parse_packet(bits: list[int]):
    version, bits = bin_to_dec(bits[:3]), bits[3:]
    type_id, bits = bin_to_dec(bits[:3]), bits[3:]

    version_sum = version

    if type_id == 4:
        value, bits = parse_literal_packet(bits)
    else:
        version, value, bits = parse_operator_packet(bits, type_id)
        version_sum += version

    return version_sum, value, bits


def parse_packets(bits: list[int]):
    values = []
    version_sum = 0

    while any(bits):
        version, value, bits = parse_packet(bits)

        values.append(value)
        version_sum += version

    return version_sum, values, bits


def part_01(bits: str):
    bits = hex_to_bin(bits)
    version, _, _ = parse_packets(bits)
    return version


def part_02(bits: str):
    bits = hex_to_bin(bits)
    _, value, _ = parse_packets(bits)
    return value[0]


input_values = utils.read("input.txt")[0]


assert part_01("38006F45291200") == 9
assert part_01("EE00D40C823060") == 14
assert part_01("8A004A801A8002F478") == 16
assert part_01("620080001611562C8802118E34") == 12
assert part_01("C0015000016115A2E0802F182340") == 23
assert part_01("A0016C880162017C3686B18A3D4780") == 31
print("Part 01:", part_01(input_values))


assert part_02("32F5DF3B128") == 123456789
assert part_02("C200B40A82") == 3
assert part_02("04005AC33890") == 54
assert part_02("880086C3E88112") == 7
assert part_02("CE00C43D881120") == 9
assert part_02("D8005AC2A8F0") == 1
assert part_02("F600BC2D8F") == 0
assert part_02("9C005AC2F8F0") == 0
assert part_02("9C0141080250320F1802104A08") == 1

print("Part 02:", part_02(input_values))
