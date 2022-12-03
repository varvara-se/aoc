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
                score += 4
            elif second == 'Y':
                score += 8
            else:
                score += 3
        case 'B':
            if second == 'Y':
                score += 5
            elif second == 'Z':
                score += 9
            else:
                score += 1
        case 'C':
            if second == 'X':
                score += 7
            elif second == 'Y':
                score += 2
            else:
                score += 6

print(score)
