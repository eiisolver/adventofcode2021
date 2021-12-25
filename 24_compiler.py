def compile(instructions):
    ix = 0
    output = []
    for instr in instructions:
        fn = instr[0]
        a = instr[1]
        if fn == 'inp':
            if ix > 0:
                output.append('    return z;')
                output.append('}')
            output.append('')
            output.append(f'long long f{ix}(long z0, int input) ' + '{')
            output.append('    z = z0;')
            output.append(f'    {a} = input;')
            ix += 1
        else:
            b = instr[2]
            if fn == 'add':
                s = f'    {a} += {b};'
            elif fn == 'mul':
                s = f'    {a} *= {b};'
            elif fn == 'div':
                s = f'    {a} /= {b};'
            elif fn == 'mod':
                s = f'    {a} = {a} % {b};'
            elif fn == 'eql':
                s = f'    {a} = {a} == {b} ? 1 : 0;'
            output.append(s)
    output.append('    return z;')
    output.append('}')
    for s in output:
        print(s)

instructions =  [line.split() for line in open('24_input.txt', 'r').read().splitlines()]
compile(instructions)
