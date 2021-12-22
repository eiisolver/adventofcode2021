
import copy
import numpy as np
import re

def overlap(r1, r2):
    """Returns overlapping range, None if no overlap"""
    r = (max(r1[0], r2[0]), min(r1[1], r2[1]))
    #print('overlap ', r1, r2, '->', r)
    return r if r[1] > r[0] else None

def split_range(r, intersect_range):
    """Splits r, example: split_range((0,10),(3,5)) returns [(0,3),(3,5),(5,10)]"""
    ranges = []
    if r[0] < intersect_range[0]:
        ranges.append((r[0], intersect_range[0]))
    ranges.append(intersect_range)
    if intersect_range[1] < r[1]:
        ranges.append((intersect_range[1], r[1]))
    return ranges

class Cube(object):
    def __init__(self, value, range):
        self.value = value
        self.range = range
        self.superseeded = False # If True, the cube has been split up in sub cubes

    def intersection(self, c):
        """Returns None if no overlap"""
        intersect_range = []
        for i in range(3):
            r = overlap(self.range[i], c.range[i])
            if r is None:
                return None
            intersect_range.append(r)
        return Cube(c.value, intersect_range)

    def split_in_sub_cubes(self, intersect_cube):
        """Returns list of up to 26 smaller cubes, none overlapping with intersect_cube"""
        cubes = []
        all_ranges = [split_range(self.range[i], intersect_cube.range[i]) for i in range(3)]
        for x_range in all_ranges[0]:
            for y_range in all_ranges[1]:
                for z_range in all_ranges[2]:
                    if x_range != intersect_cube.range[0] or y_range != intersect_cube.range[1] or z_range != intersect_cube.range[2]:
                        cubes.append(Cube(self.value, [x_range, y_range, z_range]))
        self.superseeded = True
        return cubes

    def size(self):
        return np.prod([r[1] - r[0] for r in self.range])

    def __repr__(self):
        return f'(v:{self.value}, r:{self.range}, size:{self.size()}, {", superseeded" if self.superseeded else ""})'


def count_ones(cubes):
    sub_cubes = [] # List of sub-cubes, all having value 1, none intersecting with each other
    for c in cubes:
        added_cubes = []
        for c2 in sub_cubes:
            if c2.superseeded:
                continue
            intersect = c.intersection(c2)
            if intersect is not None:
                # c intersects with c2: split c2
                added_cubes += c2.split_in_sub_cubes(intersect)
        sub_cubes += added_cubes
        if c.value == 1:
            sub_cubes.append(c) # add c, unsplit
    nr_1 = sum(c.size() for c in sub_cubes if not c.superseeded)
    print("Number of ones:", nr_1)

lines = open('22_input.txt', 'r').read().splitlines()
all_cubes = []
part1_cubes = []
for line in lines:
    nrs = [int(x) for x in re.findall('-?\d+', line)]
    cube = Cube(1 if line[1] == 'n' else 0, [(nrs[0], nrs[1] + 1), (nrs[2], nrs[3] + 1), (nrs[4], nrs[5] + 1)])
    all_cubes.append(cube)
    if max([abs(x) for x in nrs]) <= 50:
        part1_cubes.append(copy.deepcopy(cube))

count_ones(part1_cubes)
count_ones(all_cubes)
