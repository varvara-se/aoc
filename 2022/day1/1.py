s = 0
res = []

with open('./input.txt', 'r', encoding='UTF-8') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

for line in lines:
    if line == '':
        res.append(s)
        s = 0
        continue
    s += int(line)

    if line == lines[-1]:
        res.append(s)

print(max(res))
