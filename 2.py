
def product_hor_dep(arr):
    v = []
    for command in ['down', 'up', 'forward']:
        v.append(sum(amount for cmd, amount in arr if cmd == command)) 
    print('product:', (v[0] - v[1]) * v[2])

def product_hor_dep_with_aim(arr):
    hor = 0
    depth = 0
    aim = 0
    for cmd, amount in arr:
        if cmd == 'forward':
            hor += amount
            depth += aim * amount
        elif cmd == 'down':
            aim += amount
        elif cmd == 'up':
            aim -= amount
    print('product with aim:', hor * depth)

with open('2_input.txt') as f:
    arr = []
    for line in f.readlines():
        toks = line.split()
        arr.append((toks[0], int(toks[1])))

product_hor_dep(arr)
product_hor_dep_with_aim(arr)
