import collections

def step(polymer, rules):
    result = polymer
    for rule in rules:
        rep = rule[0:2]
        rep_by = rule[0] + rule[-1].lower() + rule[1]
        # 'BBBB'.replace('BB', 'BcB') -> 'BcBBcB', not 'BcBcBcB' :(
        result = result.replace(rep, rep_by).replace(rep, rep_by)
    return result.upper()

with open('14_input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    polymer = lines[0]
    rules = lines[2:]
    for _ in range(10):
        polymer = step(polymer, rules)
    counts = collections.Counter(polymer).most_common()
    print('Most common minus least common:', counts[0][1] - counts[-1][1])
