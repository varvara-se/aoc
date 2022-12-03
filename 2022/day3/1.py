score = 0
unique_char = ''

with open('./input.txt') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

for line in lines:
    middle = len(line)//2
    comp1 = line[:middle]
    comp2 = line[middle:]
    unique_char = list(set(comp1).intersection(comp2))[0]

    subtract = 38 if unique_char.isupper() else 96
    score += ord(unique_char) - subtract

print(score)
