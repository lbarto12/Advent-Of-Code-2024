from typing import List

def count_xmas(board: List[str]) -> int:
    return sum([line.count('XMAS') + line.count('SAMX') for line in board])

def transpose(mtx: List[str]) -> List[str]:
    return [''.join(s) for s in zip(*mtx)]


with open('input.txt') as file:
    lines: List[str] = [i.strip() for i in file.readlines()]

    print(f"Part 1: {count_xmas(lines) + count_xmas(t := transpose(lines)) + count_xmas(transpose(['0' * (len(t) - i) + t[i] + '0' * i for i, _ in enumerate(t)])) + count_xmas(transpose(['0' * i + t[i] + '0' * (len(t) - i) for i, _ in enumerate(t)]))}")

    # fuck checking out of bounds ;)
    w: List[str] = (p := ['0' * (len(lines[0]) + 2)]) + ['0' + i + '0' for i in lines] + p
    print(f"Part 2: {sum(w[i][j] == 'A' and {w[i - 1][j - 1], w[i + 1][j + 1]} == {w[i - 1][j + 1], w[i + 1][j - 1]} == {'M', 'S'} for j, _ in enumerate(w[0]) for i, _ in enumerate(w))}")


