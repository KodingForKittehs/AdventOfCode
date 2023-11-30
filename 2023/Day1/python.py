import unittest

def problem():
    best = 0
    sum = 0
    sums = []

    with open('Day1/input.txt') as file:
        for i in file.readlines():
            if i.strip() == '':
                best = max(best, sum)
                sums.append(sum)
                sum = 0
            else:
                sum += int(i)
    ss = sorted(sums)
    return best, ss[-1] + ss[-2] + ss[-3]


class ProblemTestCase(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(problem()[0], 70369)

    def test_problem2(self):
        self.assertEqual(problem()[1], 203002)


if __name__ == '__main__':
    unittest.main()
