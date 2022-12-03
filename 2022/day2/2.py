score = 0
with open('./input.txt') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]
    lines = tuple(i.split('\n', 1)[0] for i in lines)

for line in lines:
    first = line[0]
    second = line[2]

    match first:
        case 'A':
            if second == 'X':
                score += 3
            elif second == 'Y':
                score += 4
            else:
                score += 8
        case 'B':
            if second == 'Y':
                score += 5
            elif second == 'Z':
                score += 9
            else:
                score += 1
        case 'C':
            if second == 'X':
                score += 2
            elif second == 'Y':
                score += 6
            else:
                score += 7

print(score)
