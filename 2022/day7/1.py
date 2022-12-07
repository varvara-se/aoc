result = 0

with open('./input.txt') as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

sub_dirs = []
path_sizes_dict = {}

for line in lines:
    is_file = line.split()[0].isnumeric()

    if line.endswith('..'):
        sub_dirs = sub_dirs[:-1]
    elif line.startswith('$ cd'):
        sub_dirs.append(line.split()[2])
    elif is_file:
        file_size = int(line.split()[0])
        for i in range(len(sub_dirs)):
            path = '/'.join(sub_dirs[1:i+1])
            if path in path_sizes_dict:
                path_sizes_dict[path] += file_size
            else:
                path_sizes_dict[path] = file_size

result = sum([size for size in path_sizes_dict.values() if size < 100001])
print(result)
