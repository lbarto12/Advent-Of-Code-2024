from heapq import heappush, heappop
from typing import List, Tuple, Set

Coord = Velocity = Tuple[int, int]
Move = Tuple[int, Coord, Velocity, Set[Coord]]

DIRS: Tuple[Velocity, ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))

def t_add(a: Coord, b: Velocity) -> Coord:
    return a[0] + b[0], a[1] + b[1]

def fork(v: Velocity) -> Tuple[Velocity, Velocity]:
    return (v[1], -v[0]), (-v[1], v[0])

def find_critical_points(maze: List[str]) -> Tuple[Coord, Coord]:
    start = end = (-1, -1)
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (j, i)
            elif cell == 'E':
                end = (j, i)
    return start, end

# bfs with min-heap. vital that score is stored first in 'Move'
def find_min_path(maze: List[str]) -> Tuple[int, int]:
    start, end = find_critical_points(maze)
    heap: List[Move] = [(0, (1, 0), start, {start})]
    visited: Set[Coord, Velocity] = set[Coord, Velocity]()
    paths: Set[Coord] = set()
    lowest: int = 0


    while heap:
        score, velocity, pos, tiles = heappop(heap)

        if lowest and lowest < score:
            break

        if pos == end:
            lowest = score
            paths |= tiles
            continue

        visited.add((pos, velocity))

        x, y = t_add(pos, velocity)
        if maze[y][x] != '#' and ((x, y), velocity) not in visited:
            heappush(heap, (score + 1, velocity, (x, y), tiles | {(x, y)}))

        for nv in fork(velocity):
            if (pos, nv) not in visited:
                heappush(heap, (score + 1000, nv, pos, tiles))

    return lowest, len(paths)


with open('input.txt') as file:
    board: List[str] = [i.strip() for i in file.readlines()]

    print('Part 1: {}\nPart 2: {}'.format(*find_min_path(board)))


