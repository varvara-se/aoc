import enum
import ast

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
            return PacketOrder.left_less_than_right
        elif left > right:
            return PacketOrder.left_greater_than_right
        else:
            return PacketOrder.left_equal_to_right
    elif isinstance(left, int) and isinstance(right, list):
        return compare_packets([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare_packets(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            packet_order = compare_packets(l, r)
            if packet_order != PacketOrder.left_equal_to_right:
                return packet_order
        if len(left) < len(right):
            return PacketOrder.left_less_than_right
        elif len(left) > len(right):
            return PacketOrder.left_greater_than_right
        else:
            return PacketOrder.left_equal_to_right


dict = {}
pair_index = 0
for index in range(0, len(lines), 2):
    pair_index += 1
    left_packet = lines[index]
    right_packet = lines[index+1]

    result = compare_packets(left_packet, right_packet)
    if result == PacketOrder.left_less_than_right:
        dict[pair_index] = (left_packet, right_packet)

print(sum(dict.keys()))
