result = ''

stacks = [['B', 'W', 'N'],
          ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
          ['Q', 'H', 'Z', 'W', 'R'],
          ['W', 'D', 'V', 'J', 'Z', 'R'],
          ['S', 'H', 'M', 'B'],
          ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
          ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
          ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
          ['Z', 'W', 'M', 'S', 'C', 'D', 'J']]

with open('./input.txt') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

for line in lines:
    commands = line.split(',')
    for command in commands:
        words = command.split()
        amount = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])

        for a in range(amount):
            index = len(stacks[from_stack-1]) - (amount - a)
            item = stacks[from_stack-1][index]
            stacks[from_stack-1].pop(index)
            stacks[to_stack-1].append(item)

for stack in stacks:
    result += stack[-1]

print(result)
