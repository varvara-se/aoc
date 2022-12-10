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

result = 20*X[19] + 60*X[59] + 100*X[99] + 140*X[139] + 180*X[179] + 220*X[219]
print(result)
