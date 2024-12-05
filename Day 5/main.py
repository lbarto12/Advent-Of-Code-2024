from typing import Dict, List, Tuple

def is_report_valid(rules: Dict[int, List[int]], report: List[int]) -> bool:
    return not any(not all(report.index(rule) > index for rule in rules[page] if rule in report) for index, page in enumerate(report) if page in rules)

def count_valid(rules: Dict[int, List[int]], reports: List[List[int]]) -> int:
    return sum(report[len(report) // 2] for report in reports if is_report_valid(rules, report))

def fix(report: List[int], rules: Dict[int, List[int]]) -> List[int]:
    n, p = len(report), 0
    while p < n:
        m = p
        _ = [m := k for k in range(p, n) if report[k] in rules and report[p] in rules[report[k]]]   # ;)
        if p != m:
            report = report[:p] + report[p + 1:m + 1] + [report[p]] + report[m + 1:]
            continue
        p += 1
    return report

def count_and_fix(rules: Dict[int, List[int]], reports: List[List[int]]) -> int:
    return sum(list(n := fix(report, rules))[len(n) // 2] for report in reports if not is_report_valid(rules, report))


with open('input.txt') as file:
    lines: List[str] = file.readlines()
    r_rules, reports = lines[:(i := lines.index('\n'))], [[int(i) for i in j.split(',')] for j in lines[i + 1:]]
    t_rules: List[Tuple[int, int]] = [(int((s := i.split('|'))[0]), int(s[1])) for i in r_rules]
    rules: Dict[int, List[int]] = {}
    for r, a in t_rules:
        rules.setdefault(r, []).append(a)

    print(f'Part 1: {count_valid(rules, reports)}')

    print(f'Part 2: {count_and_fix(rules, reports)}')

