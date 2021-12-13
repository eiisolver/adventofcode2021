import numpy as np

def auto_complete_score(stack):
    v = 0
    while stack:
        v = 5 * v + {'<': 4, '(': 1, '{': 3, '[': 2}[stack.pop()]
    return v

def parse(exp):
    value = 0
    stack = []
    for c in exp:
        if c in "<{[(":
            stack.append(c)
        else:
            expected = {'<': '>', '(': ')', '{': '}', '[': ']'}[stack[-1]]
            if c == expected:
                stack.pop()
            else:
                value =  {')': 3, ']': 57, '}': 1197, '>': 25137}[c]
                break
    return value, auto_complete_score(stack)

sum_values = 0
completion_scores = []
for expr in open('10_input.txt', 'r').read().splitlines():
    v, score = parse(expr)
    sum_values += v
    if v == 0 and score != 0:
        completion_scores.append(score)
print("Sum of syntax errors:", sum_values)
print("Auto complete middle score:", np.median(completion_scores))
