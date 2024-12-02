
def valid(diff) -> bool:
    return (all(i > 0 for i in diff) or all(i < 0 for i in diff)) and all(1 <= i <= 3 for i in map(abs, diff))


with open('input.data') as file:
    lines = [list(map(int, a.split())) for a in file.readlines()]
    diffs = [[a[i] - a[i + 1] for i in range(len(a) - 1)] for a in lines]

    print(f'Part 1: {sum(valid(diff) for diff in diffs)}')

    # Absolute Degeneracy
    print(f'Part 2: {sum(valid(diff) or (any(valid([x[j] - x[j + 1] for j in range(len(x) - 1)]) for x in [lines[i][:k] + lines[i][k + 1:] for k in range(len(lines[i]))])) for i, diff in enumerate(diffs))}')

