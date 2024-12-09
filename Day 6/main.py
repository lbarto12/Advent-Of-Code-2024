from typing import List, Tuple, Set

Coord = Dir = Tuple[int, int]
Map = List[List[chr]]

# Utility functions

# Merge tuples
def add_t(a: Tuple, b: Tuple) -> Tuple:
    return a[0] + b[0], a[1] + b[1]

# Rotate Direction Clockwise
def rotate(a: Dir) -> Dir:
    return -a[1], a[0]

# Get initial guard position
def get_start(b: Map) -> Coord:
    for y, r in enumerate(b):
        for x, c in enumerate(r):
            if c == '^':
                return x, y
    return -1, -1

# Part 1
def walk(s: Coord, b: Map) -> Tuple[Map, int]:
    new: Map = [i[:] for i in b]
    n, m = len(b), len(b[0])
    x, y = s
    dr: Dir = (0, -1)
    stepped: Set[Coord] = set()

    while 0 <= x < n and 0 <= y < m:
        new[y][x] = 'X'
        stepped.add((x, y))
        xs, ys = add_t((x, y), dr)
        if not (0 <= xs < n and 0 <= ys < m):
            break
        if new[ys][xs] == '#':
            dr = rotate(dr)
            continue
        x, y = xs, ys
    return new, len(stepped)


# Part 2: Initial thoughts
#   - Add an obstacle to every empty slot in perms
#   - Check the perm with the condition: 'have I been in this spot, with the same dir before?'
#   - If so, it's a loop, and added to total possibilities
# Further Considerations
#   - Permutations only need to be created from the paths of the initial walk, since the guard will never visit others
def gen_boards(b: Map) -> List[Map]:
    boards: List[Map] = []
    w, _ = walk(get_start(b), b)
    for i, row in enumerate(w):
        for j, cell in enumerate(row):
            if cell == 'X':
                cpy = [i[:] for i in b]
                cpy[i][j] = '#'
                boards.append(cpy)
    return boards


def has_loop(s: Coord, b: Map) -> bool:
    n, m = len(b), len(b[0])
    x, y = s
    dr: Dir = (0, -1)
    seen: Set[Tuple[Coord, Dir]] = set()
    while 0 <= x < n and 0 <= y < m:
        xs, ys = add_t((x, y), dr)
        if not (0 <= xs < n and 0 <= ys < m):
            break
        if b[ys][xs] == '#':
            dr = rotate(dr)
            continue
        if ((x, y), dr) in seen:
            return True
        seen.add(((x, y), dr))
        x, y = xs, ys
    return False

def create_obstacles(s: Coord, b: Map) -> int:
    boards: List[Map] = gen_boards(b)
    count: int = 0
    for p in boards:
        if has_loop(s, p):
            count += 1
    return count


with open('input.txt') as file:
    board: Map = [list(i.strip()) for i in file.readlines()]

    _, steps = walk(get_start(board), board)
    print(f'Part 1: {steps}')

    print(f'Part 2: {create_obstacles(get_start(board), board)}')
