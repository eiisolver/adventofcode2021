from collections import namedtuple
import copy

Value = namedtuple('Value', 'value depth list index parent parent_index')

def get_values(nr, parent, parent_index, depth, values):
    for i, nr2 in enumerate(nr):
        if isinstance(nr2, list):
            get_values(nr2, nr, i, depth + 1, values)
        else:
            values.append(Value(nr2, depth, nr, i, parent, parent_index))

def to_str(nr):
    return str(nr).replace(' ', '')

def magnitude(nr):
    v = []
    for nr2 in nr:
        if isinstance(nr2, list):
            v.append(magnitude(nr2))
        else:
            v.append(nr2)
    return 3*v[0] + 2*v[1]

def reduce(nr):
    while True:
        values = []
        get_values(nr, None, None, 0, values)
        explodes = [i for i in range(len(values)) if values[i].depth >= 4]
        if explodes: # explode
            i = explodes[0]
            n = values[i]
            n.parent[n.parent_index] = 0
            if i > 0:
                prev = values[i-1]
                prev.list[prev.index] += n.value
            if i + 2 < len(values):
                nxt = values[i+2]
                nxt.list[nxt.index] += n.list[n.index+1]
            n.list[n.index] = 0
            continue

        splits = [i for i in range(len(values)) if values[i].value >= 10]
        if splits: # split
            n = values[splits[0]]
            left = n.value // 2
            n.list[n.index] = [left, n.value - left]
            continue
        return

def sum_all(lines):
    nrs = [eval(line) for line in lines]
    sum = nrs[0]
    for i in range(1, len(nrs)):
        sum = [sum, nrs[i]]
        reduce(sum)
    print('Magnitude sum of all:', magnitude(sum))

def largest_sum(lines):
    largest = 0
    nrs = [eval(line) for line in lines]
    for i in range(len(nrs)):
        for j in range(len(nrs)):
            if i == j:
                continue
            n = [copy.deepcopy(nrs[i]), copy.deepcopy(nrs[j])]
            reduce(n)
            largest = max(largest, magnitude(n))
    print('Largest magnitude of sums:', largest)

lines = open('18_input.txt', 'r').read().splitlines()
sum_all(lines)
largest_sum(lines)
