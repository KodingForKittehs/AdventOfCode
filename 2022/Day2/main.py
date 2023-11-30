import unittest


def piece_score(p):
    return ord(p) - 87


def get_score(a, b):
    match a, b:
        case 'A', 'X':
            return 3 + piece_score(b)
        case 'A', 'Y':
            return 6 + piece_score(b)
        case 'A', 'Z':
            return 0 + piece_score(b)
        case 'B', 'X':
            return 0 + piece_score(b)
        case 'B', 'Y':
            return 3 + piece_score(b)
        case 'B', 'Z':
            return 6 + piece_score(b)
        case 'C', 'X':
            return 6 + piece_score(b)
        case 'C', 'Y':
            return 0 + piece_score(b)
        case 'C', 'Z':
            return 3 + piece_score(b)


def get_play(a, b):
    match a, b:
        case 'A', 'X':
            return 'Z'
        case 'A', 'Y':
            return 'X'
        case 'A', 'Z':
            return 'Y'
        case 'B', 'X':
            return 'X'
        case 'B', 'Y':
            return 'Y'
        case 'B', 'Z':
            return 'Z'
        case 'C', 'X':
            return 'Y'
        case 'C', 'Y':
            return 'Z'
        case 'C', 'Z':
            return 'X'


def problem():
    sum1 = 0
    sum2 = 0
    with open('Day2/input.txt') as file:
        for line in file.readlines():
            p = line.split()
            play = get_play(*p)
            sum1 += get_score(*p)
            sum2 += get_score(p[0], play)
    return sum1, sum2


class ProblemTestCase(unittest.TestCase):

    def test_piece_score(self):
        self.assertEqual(piece_score('X'), 1)

    def test_problem1(self):
        self.assertEqual(problem()[0], 14069)

    def test_problem2(self):
        self.assertEqual(problem()[1], 12411)


if __name__ == '__main__':
    unittest.main()
