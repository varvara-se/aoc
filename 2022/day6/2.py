result = 0

with open('./input.txt') as f:
    packets = [i.split('\n', 1)[0] for i in f.readline()]

for k, v in enumerate(packets):
    if k > len(packets) - 15:
        break
    sub_set = packets[k:k+14]
    unique = True if len(set(sub_set)) == len(sub_set) else False
    if unique:
        result = k+14
        break

print(result)
