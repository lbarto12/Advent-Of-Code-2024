from typing import List, Tuple
import numpy as np
import re

Coord = Offset = Tuple[int, int]

def t_add(a: Offset, b: Offset) -> Offset:
    return a[0] + b[0], a[1] + b[1]

class Game:
    def __init__(self, game: Tuple[int, ...]):
        self.A: Offset = (game[0], game[1])
        self.B: Offset = (game[2], game[3])
        self.prize: Coord = (game[4], game[5])

    def get_minimum_moves(self) -> int:
        mtx: List[List[int]] = list([*zip(self.A, self.B)])
        sols: List[float] = list(np.linalg.solve(mtx, self.prize))
        if (ans := round(sols[0] * 3 + sols[1], 3)).is_integer():
            return int(ans)
        return 0


with open('input.txt') as file:
    games: List[Game] = [Game(tuple(map(int, j))) for j in re.findall(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', file.read())]

    print(f'Part 1: {sum([game.get_minimum_moves() for game in games])}')
    for game in games:
        game.prize = (game.prize[0] + 10000000000000, game.prize[1] + 10000000000000)
    print(f'Part 2: {sum([game.get_minimum_moves() for game in games])}')
