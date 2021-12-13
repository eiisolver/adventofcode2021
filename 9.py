import numpy as np

def neighbours(x, y, w, h):
    offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    result = []
    for offset in offsets:
        i, j = x + offset[0], y + offset[1]
        if 0 <= i < w and 0 <= j < h:
            result.append((i, j))
    return result

def low_points(height):
    result = []
    w = len(height[0])
    h = len(height)
    for x in range(w):
        for y in range(h):
            lowest = min(height[y][x] for x, y in neighbours(x, y, w, h))
            if height[y][x] < lowest:
                result.append((x, y))
    return result

def risk_level(height):
    lows = low_points(height)
    risk = sum(height[y][x] + 1 for x, y in lows)
    print("Risk level:", risk)

def basin(height, low_point):
    w = len(height[0])
    h = len(height)
    all_points = set()
    new_points = { low_point }
    while new_points:
        all_neighbours =  { (x, y) for a, b in new_points for x, y in neighbours(a, b, w, h) if height[y][x] < 9 }
        new_points = all_neighbours - new_points - all_points
        all_points = all_points.union(new_points)
    return all_points

def basins(height):
    basin_sizes = []
    points = set()
    for x in range(len(height[0])):
        for y in range(len(height)):
            if height[y][x] < 9 and not (x, y) in points:
                b = basin(height, (x, y))
                basin_sizes.append(len(b))
                points = points.union(b)
    print('Product of sizes of 3 largest basins:', np.prod(sorted(basin_sizes)[-3:]))

height = []
for line in open('9_input.txt', 'r').read().splitlines():
    height.append([int(c) for c in line])

risk_level(height)
basins(height)
