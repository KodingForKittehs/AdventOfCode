import unittest
from functools import cmp_to_key
import pathlib

input_file = f"{pathlib.Path(__file__).parent}/input1.txt"
sample_file = f"{pathlib.Path(__file__).parent}/sample1.txt"

def in_order(a, b):
    if type(a) == int and type(b) == int:
        if a == b:
            return 0
        if a < b:
            return -1
        if a > b:
            return 1

    if type(a) == int:
        a = [a]

    if type(b) == int:
        b = [b]

    last_idx = min(len(a), len(b))
    for i in range(last_idx):
        io = in_order(a[i], b[i])
        if io != 0:
            return io

    if len(b) < len(a):
        return 1
    if len(a) < len(b):
        return -1
    return 0


def problem(input):
    packets = []
    packets.append([[2]])
    packets.append([[6]])
    with open(input) as file:
        input = [line.strip() for line in file.readlines()]

    sum = 0
    idx = 1
    for i in range(0, len(input), 3):
        first = eval(input[i])
        second = eval(input[i + 1])
        packets.append(first)
        packets.append(second)
        if in_order(first, second) != 1:
            sum += idx
        idx += 1

    sorted_packets = sorted(packets, key=cmp_to_key(in_order))
    return sum, (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


class ProblemTestCase(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(in_order([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]), -1)
        self.assertEqual(in_order([7, 7], [7]), 1)
        self.assertEqual(in_order([1, 1], 2), -1)
        samp = problem(sample_file)
        self.assertEqual(samp[0], 13)
        self.assertEqual(samp[1], 140)
        res = problem(input_file)
        self.assertEqual(res[0], 5717)
        self.assertEqual(res[1], 25935)


if __name__ == '__main__':
    unittest.main()
