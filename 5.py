import numpy as np
import re

def points(line):
    h_sign = np.sign(line[2] - line[0])
    v_sign = np.sign(line[3] - line[1])
    p = []
    point = (line[0], line[1])
    last = (line[2], line[3])
    p.append(point)
    while point != last:
        point = (point[0] + h_sign, point[1] + v_sign)
        p.append(point)
    return p

def busy_hor_ver_spots(lines):
    at_least1 = set()
    at_least2 = set()
    for line in lines:
        if line[0] == line[2] or line[1] == line[3]:
            for point in points(line):
                if point in at_least1:
                    at_least2.add(point)
                else:
                    at_least1.add(point)
    print('Hor/ver lines: spots where >= 2 lines overlap:', len(at_least2))

def busy_hor_ver_diag_spots(lines):
    at_least1 = set()
    at_least2 = set()
    for line in lines:
        for point in points(line):
            if point in at_least1:
                at_least2.add(point)
            else:
                at_least1.add(point)
    print('All lines: spots where >= 2 lines overlap:', len(at_least2))

with open('5_input.txt') as f: 
    lines = [np.asarray(re.split('[, \->]+', line.strip()), np.int64) for line in f.readlines()]

busy_hor_ver_spots(lines)
busy_hor_ver_diag_spots(lines)
