from functools import cache
from typing import List

# Dynamic Programming saves the day
@cache
def blink(stone, blinks, d = 0) -> int:
    return d == blinks or \
        (stone == 0 and blink(1, blinks, d + 1)
            or (sz := len(s := str(stone))) % 2 == 0 and blink(int(s[:sz // 2]), blinks, d + 1) + blink(int(s[sz // 2:]), blinks, d + 1)) \
            or blink(stone * 2024, blinks, d + 1)


with open('input.txt') as file:
    line: List[int] = list(map(int, file.read().strip().split()))

    print(f'Part 1: {sum([blink(i, 25) for i in line])}')
    print(f'Part 2: {sum([blink(i, 75) for i in line])}')