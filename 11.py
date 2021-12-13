import numpy as np

flashes = 0

def flash(level, x, y):
    global flashes
    level[y][x] += 1
    if level[y][x] == 10:
        flashes += 1
        for i in range(max(0, x - 1), min(len(level[0]), x + 2)):
            for j in range(max(0, y - 1), min(len(level), y + 2)):
                flash(level, i, j)

def step(level):
    for x in range(len(level[0])):
        for y in range(len(level)):
            flash(level, x, y)
    level[level > 10] = 0

def step100(level):
    for _ in range(100):
        step(level)
    print('Number of flashes after 100 steps:', flashes)

def step_until_sync(level):
    i = 0
    while np.any(level):
        step(level)
        i += 1
    print('Synchronized after step:', i)


level = []
for line in open('11_input.txt', 'r').read().splitlines():
    level.append([int(c) for c in line])

step100(np.asarray(level, np.int32))
step_until_sync(np.asarray(level, np.int32))
