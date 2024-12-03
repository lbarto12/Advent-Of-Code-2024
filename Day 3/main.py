import re

with open('input.txt') as file:
    lines = file.read()

    print('Part 1:', sum([a * b for a, b in [(int(c), int(d)) for c, d in re.findall(r'mul\((\d+),(\d+)\)', lines)]]))

    # I AM HIM
    print('Part 2:', exec("on = True"), '\b' * 6,  sum([int(a) * int(b) for inst, a, b in re.findall(r"(don't|do|mul\((\d+),(\d+)\))", lines) if ((on := inst == 'do') and False if not inst.startswith('mul') else on)]))
