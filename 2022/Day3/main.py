import unittest
import pathlib

input_file = f"{pathlib.Path(__file__).parent}/input.txt"
input = [line.strip() for line in open(input_file).readlines()]


def priority(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def problem1():
    result = 0
    for line in input:
        s = set()
        for i, c in enumerate(line):
            if i < (len(line) // 2):
                s.add(c)
            else:
                if c in s:
                    result += priority(c)
                    break
    return result


def problem2():
    result = 0
    for bags in chunks(input, 3):
        for c in bags[0]:
            if c in bags[1] and c in bags[2]:
                result += priority(c)
                break
    return result


class ProblemTestCase(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(problem1(), 8139)

    def test_problem2(self):
        self.assertEqual(problem2(), 2668)


if __name__ == '__main__':
    unittest.main()
