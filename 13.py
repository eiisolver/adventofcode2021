
def fold_value(v, fold_value):
    return v if v <= fold_value else 2 * fold_value - v

def fold(dots, instr):
    if instr[0] == 'x':
        return {(fold_value(x[0], instr[1]), x[1]) for x in dots}
    else:
        return {(x[0], fold_value(x[1], instr[1])) for x in dots}

def part1(dots, instruction):
    print('Visible after fold 1', len(fold(dots, instruction)))

def part2(dots, instructions):
    for inst in instructions:
        dots = fold(dots, inst)
    w = max(x[0] for x in dots) + 1
    h = max(x[1] for x in dots) + 1
    print('Result of all folds:')
    for y in range(h):
        for x in range(w):
            c = '#' if (x, y) in dots else ' '
            print(c, end='')
        print()

with open('13_input.txt') as f:
    dots = set()
    instructions = []
    for line in f.readlines():
        if ',' in line:
            toks = line.strip().split(',')
            dots.add((int(toks[0]), int(toks[1])))
        elif '=' in line:
            toks = line.strip().split('=')
            instructions.append((toks[0][-1], int(toks[1])))
    part1(dots, instructions[0])
    part2(dots, instructions)
