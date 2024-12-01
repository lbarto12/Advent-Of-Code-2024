from typing import List

with open('input.txt') as file:
    lines: List[List[int]] = [list(map(int, i.split())) for i in file.readlines()]

    left: List[int] = list(sorted([a[0] for a in lines]))
    right: List[int] = list(sorted([a[1] for a in lines]))

    print(f'Part 1: {sum([abs(a - b) for a, b in list(zip(left, right))])}')

    print(f'Part 2: {sum([right.count(i) * i for i in left])}')

