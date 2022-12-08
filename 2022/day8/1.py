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
for index, row in enumerate(input):
    for pos, row_element in enumerate(row):
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

        if not vertical_up or not vertical_down or not horizontal_left or not horizontal_right:
            result += 1
            continue
        if (current > max(vertical_up) or 
            current > max(vertical_down) or 
            current > max(horizontal_left) or
            current > max(horizontal_right)):
            result += 1
       
print(result)
