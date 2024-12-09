from typing import Tuple, List

def can_solve(attempt: Tuple[int, Tuple[int, ...]], r: int = 0) -> bool:
    sm, nums = attempt
    return can_solve((sm, n := nums[1:]), nums[0] * (r or 1)) or can_solve((sm, n), nums[0] + r) if nums else r == sm


def can_solve_concat(attempt: Tuple[int, Tuple[int, ...]], r: int = 0) -> bool:
    sm, nums = attempt
    return can_solve_concat((sm, n := nums[1:]), nums[0] * (r or 1)) or \
           can_solve_concat((sm, n), nums[0] + r) or \
           can_solve_concat((sm, n), int(str(r) + str(nums[0]))) if nums else r == sm


with open('input.txt') as file:
    eqs: List[Tuple[int, Tuple[int, ...]]] = [(int((n := i.split(':'))[0]), tuple(int(j) for j in n[1].split())) for i in file.readlines()]

    print(f'Part 1: {sum([eq[0] for eq in eqs if can_solve(eq)])}')

    print(f'Part 2: {sum([eq[0] for eq in eqs if can_solve_concat(eq)])}')
