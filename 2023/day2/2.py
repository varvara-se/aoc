res = 0

with open('./input.txt', 'r', encoding='UTF-8') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

games = []
for line in lines:
    games += [line.split(':')[1]]

parsed = []
for game in games:
    g = game.replace(';','').replace(',','').strip().split(' ')
    cubes_dict = {}
    for index in range(0,len(game),2):
        for colour in g[index+1::2]:
            cubes_dict.setdefault(colour, []).append(int(g[index]))
            break
    parsed += [cubes_dict]

for p in parsed:
    res += max(p['red']) * max(p['green']) * max(p['blue']) 

print(res)
