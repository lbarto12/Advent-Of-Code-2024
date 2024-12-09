from typing import List, Dict, Tuple, Set

Coord = Vector = Tuple[int, int]

def add_t(a: Vector, b: Vector) -> Vector:
    return a[0] + b[0], a[1] + b[1]

def scalar_t(s: int, v: Vector) -> Vector:
    return s * v[0], s * v[1]

def link_antennae(board: List[str]) -> List[List[Coord]]:
    result: Dict[chr, List[Coord]] = {}
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell != '.':
                result.setdefault(cell, []).append((j, i))
    return list(result.values())

def generate_anti_nodes(nodes: List[Coord], dim: Vector, base: int = 1, extend: int = 2) -> Set[Coord]:
    anodes: Set[Coord] = set()
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            delta: Vector = (a[0] - b[0], a[1] - b[1])
            for factor in range(base, extend):
                anodes.add(add_t(a, scalar_t(factor, delta)))
                anodes.add(add_t(b, scalar_t(factor, (-delta[0], -delta[1]))))
    return set(filter(lambda c: 0 <= c[0] < dim[0] and 0 <= c[1] < dim[1], anodes))


with open('input.txt') as file:
    lines: List[str] = [i.strip() for i in file.readlines()]
    n, m = len(lines), len(lines[0])
    antennae: List[List[Coord]] = link_antennae(lines)

    anti_nodes: Set[Coord] = set()
    for antenna in antennae:
        anti_nodes = anti_nodes.union(generate_anti_nodes(antenna, (m, n)))
    print(f'Part 1: {len(anti_nodes)}')

    anti_nodes = set()
    for antenna in antennae:
        anti_nodes = anti_nodes.union(generate_anti_nodes(antenna, (m, n), 0, max(m, n)))
    print(f'Part 2: {len(anti_nodes)}')
