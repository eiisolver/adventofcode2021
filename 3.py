from functools import reduce

def gamma_times_epsilon(lines):
    nr_bits = len(lines[0])
    most_common = []
    for i in range(nr_bits):
        count = sum(line[i] == '1'  for line in lines)
        most_common.append(2*count >= len(lines))
    gamma = reduce(lambda a, b: (a<<1) + int(b), most_common)
    epsilon = (1 << nr_bits) - gamma - 1
    print('gamma:', gamma, ', epsilon:', epsilon)
    print('gamma * epsilon:', gamma * epsilon)

def filter(lines, index, use_most):
    nr_1 = sum(line[index] == '1' for line in lines)
    if (use_most and 2*nr_1 >= len(lines)) or (not use_most and 2*nr_1 < len(lines)):
        to_keep = '1'
    else:
        to_keep = '0'
    return [line for line in lines if line[index] == to_keep]

def filter_until_1_left(lines, use_most):
    for i in range(len(lines[0])):
        lines = filter(lines, i, use_most)
        if len(lines) == 1:
            return int(lines[0], 2)

def part2(lines):
    oxygen = filter_until_1_left(lines, True)
    co2 = filter_until_1_left(lines, False)
    print('oxygen:', oxygen, ', co2:', co2)
    print('oxygen * CO2:', oxygen * co2)

with open('3_input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

gamma_times_epsilon(lines)
part2(lines)
