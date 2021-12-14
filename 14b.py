def add(dic, key, amount):
    if key in dic:
        dic[key] += amount
    else:
        dic[key] = amount

def step(pairs, rules):
    new_pairs = dict()
    for key, amount in pairs.items():
        rule = rules.get(key)
        if rule:
            add(new_pairs, rule[0], amount)
            add(new_pairs, rule[1], amount)
        else:
            add(new_pairs, key, amount)
    return new_pairs

with open('14_input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    polymer = lines[0]
    rules = {s[0:2]: (s[0] + s[-1], s[-1] + s[1]) for s in lines[2:]}
    pairs = dict()
    for i in range(len(polymer) - 1):
        add(pairs, polymer[i:i+2], 1)
    for i in range(40):
        pairs = step(pairs, rules)
    counts = dict() # frequency of individual characters
    for key, amount in pairs.items():
        add(counts, key[0], amount)
        add(counts, key[1], amount)
    # All chars are counted twice in above loop except first/last
    add(counts, polymer[0], 1)
    add(counts, polymer[-1], 1)
    freqs = sorted([amount // 2 for amount in counts.values()])
    print('Most common minus least common:', freqs[-1] - freqs[0])
