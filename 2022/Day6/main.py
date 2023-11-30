import unittest
import pathlib

input_file = f"{pathlib.Path(__file__).parent}/input.txt"

def problem(size):
    with open(input_file) as file:
        line = file.readline()
        for i, c in enumerate(line):
            s = set()
            for j in range(size):
                s.add(line[i + j])
            if len(s) == size:
                return i + size


class ProblemTestCase(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(problem(4), 1598)

    def test_problem2(self):
        self.assertEqual(problem(14), 2414)


if __name__ == '__main__':
    unittest.main()
