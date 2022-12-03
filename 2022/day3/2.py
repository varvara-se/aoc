score = 0
unique_char = ''

with open('./input.txt') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

for i in range(0, len(lines)-1, 3):
    l1 = lines[i]
    l2 = lines[i+1]
    l3 = lines[i+2]
    unique_char = list(set(l1).intersection(l2).intersection(l3))[0]

    subtract = 38 if unique_char.isupper() else 96
    score += ord(unique_char) - subtract

print(score)
