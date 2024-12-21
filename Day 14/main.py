from typing import List, Tuple, Set, Dict
import re

Coord = Velocity = Tuple[int, int]

BOARD_SIZE = (101, 103)

def t_add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]

def wrap(a: Coord) -> Coord:
    return a[0] % BOARD_SIZE[0], a[1] % BOARD_SIZE[1]

class Robot:
    def __init__(self, settings: Tuple[int, ...]):
        self.pos: Coord = settings[0], settings[1]
        self.velocity: Velocity = settings[2], settings[3]

    def step(self):
        self.pos = wrap(t_add(self.pos, self.velocity))

    def __eq__(self, other: Coord):
        return self.pos == other

    def __hash__(self):     # Hacky hash override to decrease tuple retrieval time in part 2
        return hash(self.pos)

def quadrant_score(bots: List[Robot]) -> int:
    mx, my = BOARD_SIZE[0] // 2, BOARD_SIZE[1] // 2
    quads: Dict[bool, Dict[bool, int]] = {True: {True: 0, False: 0}, False: {True: 0, False: 0}}
    for bot in bots:
        if bot.pos[0] != mx and bot.pos[1] != my:
            quads[bot.pos[0] < mx][bot.pos[1] < my] += 1
    (a, b), (c, d) = (i.values() for i in quads.values())
    return a * b * c * d

def adj_score(bots: List[Robot]) -> int:
    bots_s: Set[Robot] = set(bots)
    score: int = 0
    for bot in bots_s:
        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if t_add(bot.pos, (x, y)) in bots_s:
                score += 1
    return score


with open('input.txt') as file:
    robots: List[Robot] = list(Robot(tuple(map(int, i))) for i in re.findall(r'p=([\-0-9]+),([\-0-9]+) v=([\-0-9]+),([\-0-9]+)', file.read()))

    part_1: int = 0
    max_adj_score: Tuple[int, int] = (0, 0)
    for i in range(10000):
        if (s := adj_score(robots)) > max_adj_score[0]:
            max_adj_score = (s, i)
        if i == 100:
            part_1 = quadrant_score(robots)
        for r in robots:
            r.step()

print(f'Part 1: {part_1}')
print(f'Part 2: {max_adj_score[1]}')

