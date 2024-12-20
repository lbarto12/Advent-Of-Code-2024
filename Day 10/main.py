from typing import List, Tuple, Set

Board = List[str]
Coord = Dir = Tuple[int, int]

DIRS: List[Dir] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_starts(board: Board) -> List[Coord]:
    return [(j, i) for i, r in enumerate(board) for j, v in enumerate(r) if v == '0']

def score_trails(start: Coord, board: Board) -> Tuple[Set[Coord], int]:
    x, y = start
    if board[y][x] == '9':
        return {(x, y)}, 1
    sm: int = 0
    end: Set[Coord] = set()
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < len(board[0]) and 0 <= ny < len(board)):
            continue
        if int(board[ny][nx]) == int(board[y][x]) + 1:
            nxt, add = score_trails((nx, ny), board)
            sm += add
            end.update(nxt)
    return end, sm


with open('input.txt') as file:
    lines = [i.strip() for i in file.readlines()]

    ends, paths = list(zip(*[score_trails(start, lines) for start in get_starts(lines)]))
    print(f'Part 1: {sum(map(len, ends))}')
    print(f'Part 2: {sum(paths)}')
