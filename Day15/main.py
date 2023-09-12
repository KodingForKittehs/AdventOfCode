import sys
import re
import unittest

dirs = []

sys.abiflags


def manhatten(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def problem1_backup(input, line_num):
    beacons = set()
    cant_be = set()

    with open(input) as file:
        for line in file.readlines():
            nums = re.findall(r"\d+", line)
            sensor = int(nums[0]), int(nums[1])
            beacon = int(nums[2]), int(nums[3])
            if beacon[1] == line_num:
                beacons.add(beacon)
            dist = manhatten(sensor, beacon)
            for x in range(sensor[0] - dist, sensor[0] + dist + 1):
                p = (x, line_num)
                if manhatten(p, sensor) <= dist and p != beacon:
                    cant_be.add(x)
    print(input, len(cant_be))
    return len(cant_be)


def problem1(input, line_num):
    # Write X, B into a large enough space
    offset = 100_000_000
    cant_be = ["."] * offset * 2

    with open(input) as file:
        for line in file.readlines():
            nums = re.findall(r"\d+", line)
            sensor = int(nums[0]), int(nums[1])
            beacon = int(nums[2]), int(nums[3])
            if beacon[1] == line_num:
                cant_be[beacon[0] + offset] = "B"
            dist = manhatten(sensor, beacon)
            for x in range(sensor[0] - dist, sensor[0] + dist + 1):
                p = (x, line_num)
                if manhatten(p, sensor) <= dist and cant_be[x + offset] == ".":
                    cant_be[x] = "X"
    res = cant_be.count("X")
    print(input, res)
    return res


def problem2(input):
    pass


class ProblemTestCase(unittest.TestCase):
    def test_problem(self):
        self.assertEqual(manhatten((1, 6), (5, 3)), 7)
        self.assertEqual(manhatten((0, 0), (1, 1)), 2)
        self.assertEqual(problem1("Day15/sample1.txt", 10), 26)
        self.assertEqual(problem1("Day15/input1.txt", 2000000), 4424278)
        # self.assertGreater(problem1('Day15/input2.txt', 2000000), 2887170)

        self.assertEqual(problem2("Day15/sample1.txt"), 56000011)
        # self.assertEqual(problem2('Day15/sample1.txt'), 56000011)


if __name__ == "__main__":
    unittest.main()
