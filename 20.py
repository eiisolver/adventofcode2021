def enhance(img, algo, pad_value):
    pad = 2
    # pad image with 2 rows/columns
    w = 2 * pad + len(img[0])
    pad_y = pad * [w * pad_value]
    pad_x = pad * pad_value
    img_ext = pad_y + [pad_x + line + pad_x for line in img] + pad_y
    result = []
    for y in range(1, len(img_ext) - 1):
        s = ''
        for x in range(1, w - 1):
            v = int(img_ext[y-1][x-1:x+2] + img_ext[y][x-1:x+2] + img_ext[y+1][x-1:x+2], 2)
            s += algo[v]
        result.append(s)
    return result

def enhance_steps(img, algo, steps):
    pad_value = '0'
    for _ in range(steps):
        img = enhance(img, algo, pad_value)
        pad_value = algo[0 if pad_value == '0' else 511]
    nr_1 = sum(line.count('1') for line in img)
    print(f'Number of 1: after {steps}: {nr_1}')

lines = open('20_input.txt', 'r').read().splitlines()
lines = [line.replace('#', '1').replace('.', '0') for line in lines]

algo = lines[0]
img = [line for line in lines[1:] if len(line) > 0]

enhance_steps(img, algo, 2)
enhance_steps(img, algo, 50)
