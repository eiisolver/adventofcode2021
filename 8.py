import itertools

def nr_1_4_7_8(arr):
    n = 0
    for line in arr:
        n += sum(len(x) in (2, 3, 4, 7) for x in line[11:])
    print("nr 1/4/7/8:", n)

def to_int_list(segments):
    return [(ord(c) - ord('a')) for c in segments]

def to_bitmask(intlist):
    return sum(1 << x for x in intlist)

def sum_digits_in_line(line):
    digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    intlists = [to_int_list(digit) for digit in digits]
    pattern_set = set(to_bitmask(to_int_list(intlist)) for intlist in line[0:10])
    outputs = [to_bitmask(to_int_list(intlist)) for intlist in line[11:]]
    for permutation in itertools.permutations(range(7)):
        matches = True
        for d in range(10):
            v = to_bitmask([permutation[x] for x in intlists[d]])
            if not v in pattern_set:
                matches = False
                break
        if matches:
            sum = 0
            for output in outputs:
                for d in range(10):
                    if output == to_bitmask([permutation[x] for x in intlists[d]]):
                        sum = 10*sum + d
            return sum
    raise ValueError('No solution found!')

def sum_digits(arr):
    sum = 0
    for line in arr:
        sum += sum_digits_in_line(line)
    print('sum of all outputs:', sum)

with open('8_input.txt') as f: 
    lines = [line.split() for line in f.readlines()]

nr_1_4_7_8(lines)
sum_digits(lines)
