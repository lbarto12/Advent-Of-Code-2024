from typing import List, Tuple

def expand(f: str) -> List[chr]:
    res, gap, d = [], True, 0
    for c in f:
        res += ['.'] * int(c) if (gap := not gap) else [str(d)] * int(c)
        d += gap
    return res

def compress(f: List[chr]) -> List[int]:
    i = 0
    while i < len(f):
        while f[i] == '.':
            f[i] = f.pop()
        i += 1
    return list(map(int, f))

def grouped(f: str) -> List[Tuple[chr, int]]:
    res, gap, d = [], True, 0
    for c in f:
        res.append(('.', int(c)) if (gap := not gap) else (str(d), int(c)))
        d += gap
    return res

def attempt_shift(groups: List[Tuple[chr, int]]) -> List[Tuple[chr, int]]:
    mx: int = int(groups[-1][0])
    for i in range(len(groups) - 1, -1, -1):
        if groups[i][0] == str(mx):
            for j, (ch, c) in enumerate(groups[:i]):
                if ch == '.' and c >= groups[i][1]:
                    groups[j], groups[i] = groups[i], ('.', groups[i][1])
                    if (df := c - groups[i][1]) > 0:
                        groups.insert(j + 1, ('.', df))
                    break
            mx -= 1
    return groups

def format_shift(f: List[Tuple[chr, int]]) -> List[chr]:
    res = []
    for a, b in f:
        res += [a] * b
    return res


with open('input.txt') as file:
    filesys = file.read()

    print(f'Part 1: {sum(i * int(c) for i, c in enumerate(compress(expand(filesys))))}')
    print(f'Part 2: {sum(i * int(c) for i, c in enumerate(format_shift(attempt_shift(grouped(filesys)))) if c.isnumeric())}')
