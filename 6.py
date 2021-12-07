import numpy as np

def calc_sum(arr, days):
    unique, counts = np.unique(arr, return_counts=True)
    v = 9 * [0]
    for (x, n) in zip(unique, counts):
        v[x] = n

    for _ in range(days):
        spawned = v.pop(0)
        v[6] += spawned
        v.append(spawned)
    print('sum after', days, 'days:', sum(v))

with open('6_input.txt') as f: 
    text = f.read()

arr = np.asarray(text.strip().split(','), np.int64)

calc_sum(arr, 80)
calc_sum(arr, 256)
