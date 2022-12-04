score = 0

with open('./input.txt') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

for line in lines:
    pair1 = line.split(',')[0]
    pair2 = line.split(',')[1]

    p1_n1 = int(pair1.split('-')[0])
    p1_n2 = int(pair1.split('-')[1])
    p2_n1 = int(pair2.split('-')[0])
    p2_n2 = int(pair2.split('-')[1])

    if p1_n2 >= p2_n1 and p1_n2 <= p2_n2:
        score += 1
    elif p2_n2 >= p1_n1 and p2_n2 <= p1_n2:
        score += 1

print(score)
