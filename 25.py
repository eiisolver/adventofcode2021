import numpy as np

lines = [list(line) for line in open('25_input.txt', 'r').read().splitlines()]

step = 0
moved = True
while moved:
    step += 1
    moved = False
    for c in ['>', 'v']:
        nxt = [line.copy() for line in lines]
        h = len(lines)
        w = len(lines[0])
        for y in range(h):
            for x in range(w):
                c1 = lines[y][x]
                c2 = lines[y][(x + 1) % w]
                if c1 == c and c2 == '.':
                    nxt[y][x] = c2
                    nxt[y][(x + 1) % w] = c1
                    moved = True
        lines = np.transpose(nxt)

print('Number of steps:', step)
