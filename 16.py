import numpy as np
import operator

class Buffer(object):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def get(self, n):
        v = 0
        for i in range(self.index, self.index + n):
            v = 2*v + (1 & (self.data[i >> 3] >> (7 - (i & 7))))
        self.index += n
        return v

def parse(buf):
    version = buf.get(3)
    global version_sum
    version_sum += version
    id = buf.get(3)
    if id == 4: # literal
        value = 0
        cont = True
        while cont:
            cont = buf.get(1)
            value = (value << 4) + buf.get(4)
        return (id, value)
    else: # operator
        par = []
        length_type_id = buf.get(1)
        if length_type_id:
            packets = buf.get(11)
            for _ in range(packets):
                par.append(parse(buf))
        else:
            length = buf.get(15)
            start = buf.index
            while buf.index - start < length:
                par.append(parse(buf))
        return (id, par)

def evaluate(exp):
    id, par = exp
    if id < 4:
        op = { 0: sum, 1: np.prod, 2: min, 3: max }[id]
        v = op([evaluate(x) for x in par])
    elif id == 4:
        v = par
    else:
        op = { 5: operator.gt, 6: operator.lt, 7: operator.eq }[id]
        v = 1 if op(evaluate(par[0]), evaluate(par[1])) else 0
    return v

hex = open('16_input.txt', 'r').read().strip()
buf = Buffer(bytes.fromhex(hex))
version_sum = 0
exp = parse(buf)
print('Sum of versions:', version_sum)
print('Result of eval:', evaluate(exp))
