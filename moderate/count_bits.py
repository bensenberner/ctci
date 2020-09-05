from typing import List


def is_power_of_two(num):
    return (num & (num - 1)) == 0


def countBits(num: int) -> List[int]:
    bits = [0 for _ in range(num + 1)]
    bits[0] = 0
    curr_exponent_of_two = -1
    curr_power_of_two = 1
    for idx in range(1, num + 1):
        if is_power_of_two(idx):
            bits[idx] = 1
            curr_exponent_of_two += 1
            curr_power_of_two = 2 ** curr_exponent_of_two
            continue
        bits[idx] = bits[idx - curr_power_of_two] + 1
    return bits
