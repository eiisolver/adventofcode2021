import numpy as np

def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def check_common(s0, s1, required_common):
    for i, coord in enumerate(s0):
        if i < required_common - 1:
            continue
        for coord2 in s1:
            s1_coord = np.subtract(coord, coord2)
            s2 = {add(s1_coord, c) for c in s1}
            common = s0.intersection(s2)
            if len(common) >= required_common:
                return s1_coord, s2
    return None, None

def rot90(c, axis):
    if axis == 0:
        return (c[0], c[2], int(-c[1]))
    elif axis == 1:
        return (c[2], c[1], int(-c[0]))
    return (c[1], int(-c[0]), c[2])

def rot90x(c, axis, x):
    result = c
    for _ in range(x):
        result = rot90(result, axis)
    return result

def rotate(c, per_axis):
    result = c
    for axis in range(len(per_axis)):
        result = rot90x(result, axis, per_axis[axis])
    return result

def get_rotations():
    rotations = []
    all_rotations = [(a, b, c) for a in range(4) for b in range(4) for c in range(4)]
    c = (1, 2, 3)
    c_rotations = set()
    for rotation in all_rotations:
        c_rot = rotate(c, rotation)
        if not c_rot in c_rotations:
            rotations.append(rotation)
            c_rotations.add(c_rot)
    return rotations

def locate_scanners(scanners):
    n = len(scanners)
    location = n * [(0,0,0)] # location of the scanners
    beacons = scanners[0].copy() # all found beacons
    found = n * [False] # True if location of scanner i is known
    found[0] = True
    completed = n * [False] # True if scanner i has been matched with all other scanners
    rotations = get_rotations()
    stop = False
    while not stop:
        stop = True
        for i in range(n):
            if not found[i] or completed[i]:
                continue
            completed[i] = True
            sc1 = scanners[i]
            for j in range(n):
                if found[j]:
                    continue
                print('Match scanners', i, ' and ', j)
                sc2 = scanners[j]
                for rotation in rotations:
                    coords = {rotate(c, rotation) for c in sc2 }
                    s2_location, s2_beacons = check_common(sc1, coords, 12)
                    if s2_beacons:
                        print("Matched!, using rotation", rotation)
                        location[j] = s2_location
                        scanners[j] = {add(s2_location, c) for c in coords}
                        found[j] = True
                        beacons = beacons.union(s2_beacons)
                        print("Scanner ", j, ":", sorted(scanners[j]))
                        stop = False
                        break
    for i, c in enumerate(location):
        print('Scanner ', i, ' is at', c)
    print("All beacons:", sorted([b for b in beacons]))
    print("Nr beacons:", len(beacons))
    max_manhattan = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum(abs(location[i][a] - location[j][a]) for a in range(3))
            max_manhattan = max(max_manhattan, dist)
    print('Max manhattan distance:', max_manhattan)

lines = open('19_input.txt', 'r').read().splitlines()
scanners = []
for line in lines:
    if line.startswith('---'):
        scanner = set()
        scanners.append(scanner)
    elif len(line) > 0:
        scanner.add(tuple([int(c) for c in line.split(',')]))

locate_scanners(scanners)
