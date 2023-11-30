import unittest

input = [line.strip() for line in open('Day4/input.txt').readlines()]


def fully_overlap(str):
    a, b = str.split(',')
    amin, amax = a.split('-')
    bmin, bmax = b.split('-')
    amin, amax, bmin, bmax = int(amin), int(amax), int(bmin), int(bmax)

    if (
        (amin <= bmin and amax >= bmax)
        or (bmin <= amin and bmax >= amax)
    ):
        return True
    return False


def is_contained(start, end, value):
    return value >= start and value <= end

def any_overlap(str):
    a, b = str.split(',')
    amin, amax = a.split('-')
    bmin, bmax = b.split('-')
    amin, amax, bmin, bmax = int(amin), int(amax), int(bmin), int(bmax)

    return (
        is_contained(amin, amax, bmin)
        or is_contained(amin, amax, bmax)
        or is_contained(bmin, bmax, amin)
        or is_contained(bmin, bmax, amax)
    )


def problem1():
    sum = 0
    for line in input:
        if fully_overlap(line):
            sum += 1
    return sum

def problem2():
    sum = 0
    for line in input:
        if any_overlap(line):
            sum += 1
    return sum


class ProblemTestCase(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(problem1(), 413)

    def test_problem2(self):
        self.assertEqual(problem2(), 806)


if __name__ == '__main__':
    unittest.main()
