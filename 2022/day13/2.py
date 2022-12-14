import enum
import ast
import functools

with open('./input.txt') as f:
    # don't try this at home kids!
    lines = [ast.literal_eval(i) for i in f.readlines() if i != '\n']


class PacketOrder(enum.Enum):
    left_greater_than_right = 1
    left_less_than_right = -1
    left_equal_to_right = 0


def compare_packets(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return PacketOrder.left_less_than_right.value
        elif left > right:
            return PacketOrder.left_greater_than_right.value
        else:
            return PacketOrder.left_equal_to_right.value
    elif isinstance(left, int) and isinstance(right, list):
        return compare_packets([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare_packets(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            packet_order = compare_packets(l, r)
            if packet_order != PacketOrder.left_equal_to_right.value:
                return packet_order
        if len(left) < len(right):
            return PacketOrder.left_less_than_right.value
        elif len(left) > len(right):
            return PacketOrder.left_greater_than_right.value
        else:
            return PacketOrder.left_equal_to_right.value


lines.append([[2]])
lines.append([[6]])
lines.sort(key=functools.cmp_to_key(compare_packets))
res_1 = lines.index([[2]]) + 1
res_2 = lines.index([[6]]) + 1

print(res_1*res_2)
