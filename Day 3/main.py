import re

with open('input.txt') as file:
    lines = file.read()

    print('Part 1:', sum([a * b for a, b in [(int(c), int(d)) for c, d in re.findall(r'mul\((\d+),(\d+)\)', lines)]]))


    on = True

    def flip(inst: str) -> bool:
        global on
        current = on
        if not (m := inst.startswith('mul')):
            on = inst == 'do'
        return current and m

    print('Part 2:', sum([int(a) * int(b) for inst, a, b in re.findall(r"(don't|do|mul\((\d+),(\d+)\))", lines) if flip(inst)]))