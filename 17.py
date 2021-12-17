# target area: x=117..164, y=-140..-89
#x_min, x_max, y_min, y_max = 20, 30, -10, -5
x_min, x_max, y_min, y_max = 117, 164, -140, -89

n = -2 * y_min + 1

# Check which x velocities end up in the target area
x_solutions = [set() for _ in range(n)]

for vx in range(x_max + 1):
    velocity = vx
    x = step = 0
    while step < n - 1 and x <= x_max and (velocity > 0 or x >= x_min):
        x += velocity
        if velocity > 0:
            velocity -= 1
        step += 1
        if x_min <= x <= x_max:
            x_solutions[step].add(vx)

solutions = set()

# Check which y velocities end up in the target area
for vy in range(y_min, -y_min + 1):
    velocity = vy
    y = step = 0
    while y >= y_min:
        y += velocity
        velocity -= 1
        step += 1
        if y_min <= y <= y_max:
            for vx in x_solutions[step]:
                solutions.add((vx, vy))

print('highest y:', (y_min) * (y_min + 1) // 2)
print('hits:', len(solutions))
