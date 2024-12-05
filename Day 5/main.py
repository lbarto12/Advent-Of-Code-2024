from typing import Dict, List

import itertools

def is_report_valid(rules: Dict[int, List[int]], report: Dict[int, int]) -> bool:
    valid = True
    for page, index in report.items():
        if page not in rules:
            continue
        for rule in rules[page]:
            if rule not in report:
                continue
            if report[rule] < index:
                valid = False
                break
        if not valid:
            break
    return valid


def count_valid(rules: Dict[int, List[int]], reports: List[Dict[int, int]]) -> int:
    sm = 0
    for report in reports:
        if is_report_valid(rules, report):
            sm += list(report.keys())[len(report) // 2]
    return sm

def fix(report: Dict[int, int], rules: Dict[int, List[int]]) -> List[int]:
    n = list(report.keys())
    j = 0
    while j < len(n):
        m = j
        for k in range(j, len(n)):
            if n[k] in rules and n[j] in rules[n[k]]:
                m = k
        if j != m:
            n = n[:j] + n[j + 1:m + 1] + [n[j]] + n[m + 1:]
        if j == m:
            j += 1
    return n

def count_and_fix(rules: Dict[int, List[int]], reports: List[Dict[int, int]]) -> int:
    sm = 0
    for i, report in enumerate(reports):
        if is_report_valid(rules, report):
            continue
        else:
            sm += list(n := fix(report, rules))[len(n) // 2]
    return sm


with open('input.txt') as file:
    lines = file.readlines()
    rules, reports = lines[:(i := lines.index('\n'))], lines[i + 1:]
    _rules = [(int((s := i.split('|'))[0]), int(s[1])) for i in rules]
    rules = {}
    for k, a in _rules:
        rules.setdefault(k, []).append(a)
    reports = [[int(i) for i in j.split(',')] for j in reports]
    reports = [{k: i for i, k in enumerate(j)} for j in reports]

    print(f'Part 1: {count_valid(rules, reports)}')

    print(f'Part 2: {count_and_fix(rules, reports)}')

