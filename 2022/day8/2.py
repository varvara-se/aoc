import math

result = 0
with open('./input.txt') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

input = []
for index,line in enumerate(lines):
    curr_line = [*line]
    input.append(curr_line)

def get_column(pos, arr):
    return [row[pos] for row in arr]

vertical_up = []
vertical_down = []
horizontal_left = []
horizontal_right = []

scores = []
final_scores = []
for index, row in enumerate(input):
    for pos, row_element in enumerate(row):
        score_1 = 0
        score_2 = 0
        score_3 = 0
        score_4 = 0
        current = input[index][pos]
        if pos == 0:
            horizontal_left = []
            horizontal_right = input[index][pos+1:]
        elif pos == len(row)-1:
            horizontal_left = input[index][:pos]
            horizontal_right = []
        else:
            horizontal_left = input[index][:pos]
            horizontal_right = input[index][pos+1:]

        if index == 0:
            vertical_down = get_column(pos, input[index+1:])
            vertical_up = []
        elif index == len(input)-1:
            vertical_down = []
            vertical_up = get_column(pos, input[:index])
        else:
            vertical_down = get_column(pos, input[index+1:])
            vertical_up = get_column(pos, input[:index])

        for i in horizontal_right:
            if i < current:
                score_1 += 1
            elif i >= current:
                score_1 += 1
                break
        horizontal_left = reversed(horizontal_left)
        for i in horizontal_left:
            if i < current:
                score_2 += 1
            elif i >= current:
                score_2 += 1     
                break
        vertical_up = reversed(vertical_up)
        for i in vertical_up:
            if i < current:
                score_3 += 1         
            elif i >= current:
                score_3 += 1
                break
        for i in vertical_down:
            if i < current:
                score_4 += 1
            elif i >= current:
                score_4 += 1
                break
        scores = math.prod([score for score in [score_1, score_2, score_3, score_4]])
        final_scores.append(scores)

print(max(final_scores))

