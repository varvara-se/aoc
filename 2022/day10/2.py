result = 0

with open('./input.txt') as f:
    commands = [i.split('\n', 1)[0] for i in f.readlines()]

X = [1]
v = 1
cycle = 0
for index, command in enumerate(commands):
    previous = X[cycle]
    if command.startswith('noop'):
        X.append(previous)
        cycle += 1
    else:
        current = int(command.split()[1])
        v = previous + current
        X.append(previous)
        X.append(v)
        cycle += 2

X_1 = X[:40]
X_2 = X[40:80]
X_3 = X[80:120]
X_4 = X[120:160]
X_5 = X[160:200]
X_6 = X[200:]


def get_grid_line(cycle, register):
    crt = ''
    if cycle == register[cycle]-1 or cycle == register[cycle] or cycle == register[cycle]+1:
        crt += '#'
    else:
        crt += ' '
    return ''.join(crt)


grid = []
for cycle in range(40):
    grid.append(get_grid_line(cycle, X_1))

for cycle in range(40):
    grid.append(get_grid_line(cycle, X_2))

for cycle in range(40):
    grid.append(get_grid_line(cycle, X_3))

for cycle in range(40):
    grid.append(get_grid_line(cycle, X_4))

for cycle in range(40):
    grid.append(get_grid_line(cycle, X_5))

for cycle in range(40):
    grid.append(get_grid_line(cycle, X_6))

print(''.join(grid[:40]))
print(''.join(grid[40:80]))
print(''.join(grid[80:120]))
print(''.join(grid[120:160]))
print(''.join(grid[160:200]))
print(''.join(grid[200:241]))
