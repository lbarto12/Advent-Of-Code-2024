from typing import List, Tuple, Dict, Set
from copy import deepcopy

Board = List[List[chr]]
Coord = Velocity = Tuple[int, int]

MOVES: Dict[chr, Velocity] = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
BOX: Dict[chr, int] = {'[': 1, ']': -1}
WIDE_REMAP: Dict[chr, str] = {'@': '@.', 'O': '[]', '.': '..', '#': '##'}

def t_add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]

def setup_board(board: Board) -> Tuple[Coord, Board]:
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == '@':
                board[i][j] = '.'
                return (j, i), board
    raise ValueError('Invalid board')

def widen_board(board: Board) -> Board:
    return [list(''.join(row)) for row in [[WIDE_REMAP[i] for i in row] for row in board]]

def try_step(board: Board, pos: Coord, v: Velocity, nxt: chr) -> bool:
    x, y = t_add(pos, v)
    if board[y][x] == '#':
        return False
    if board[y][x] == '.':
        board[y][x] = nxt
        return True
    if v := try_step(board, (x, y), v, board[y][x]):
        board[y][x] = nxt
    return v

def try_step_wide(board: Board, pos: Coord, v: Velocity) -> Tuple[bool, Set[Coord]]:
    x, y = t_add(pos, v)
    if board[y][x] == '#':
        return False, set()
    if board[y][x] == '.':
        return True, set()
    if v[0] == 0:
        check_side = BOX[board[y][x]]
        a, s1 = try_step_wide(board, (x, y), v)
        b, s2 = try_step_wide(board, (x + check_side, y), v)
        return a and b, s1.union(s2).union({(x, y), (x + check_side, y)}) if a and b else set()
    r, s = try_step_wide(board, (x, y), v)
    return r, s.union({(x, y)}) if r else set()

def do_moves(board: Board, moves: str):
    pos, board = setup_board(board)
    for move in moves:
        m: Velocity = MOVES[move]
        if try_step(board, pos, m, '.'):
            pos = t_add(pos, m)

def do_moves_wide(board: Board, moves: str):
    pos, board = setup_board(board)
    for move in moves:
        m: Velocity = MOVES[move]
        can_move, blocks = try_step_wide(board, pos, m)
        if can_move:
            pos = t_add(pos, m)
            new = deepcopy(board)
            for b in blocks:
                new[b[1]][b[0]] = '.'
            for b in blocks:
                n = t_add(b, m)
                new[n[1]][n[0]] = board[b[1]][b[0]]
            board[:] = new

def score_board(board: Board, sym: chr) -> int:
    return sum((100 * i + j) for i, row in enumerate(board) for j, val in enumerate(row) if val == sym)


with open('input.txt') as file:
    lines: List[str] = file.read().split('\n\n')
    board: Board = list([list(i) for i in lines[0].split('\n')])
    moves: str = lines[1].replace('\n', '')
    widened = widen_board(board)

    do_moves(board, moves)
    do_moves_wide(widened, moves)

    print(f'Part 1: {score_board(board, "O")}')
    print(f'Part 2: {score_board(widened, "[")}')

