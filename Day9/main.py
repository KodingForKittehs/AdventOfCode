import unittest

def move(start, dir):
    return (start[0] + dir[0], start[1] + dir[1])


def move_tail(tail, head):
    if abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
        # Diagonal move
        return (head[0] + tail[0]) // 2, (head[1] + tail[1]) // 2
    if head[1] == tail[1] + 2:
        return (head[0], head[1] - 1)
    if head[1] == tail[1] - 2:
        return (head[0], head[1] + 1)
    if head[0] == tail[0] + 2:
        return (head[0] - 1, head[1])
    if head[0] == tail[0] - 2:
        return (head[0] + 1, head[1])
    return tail


def parse_line(line):
    line_items = line.split()
    step = int(line_items[1])
    if line_items[0] == 'R':
        return (0, 1), step
    if line_items[0] == 'L':
        return (0, -1), step
    if line_items[0] == 'U':
        return (1, 0), step
    if line_items[0] == 'D':
        return (-1, 0), step


def problem(rope_size):
    rope_size = rope_size
    knots = [(0, 0)] * rope_size
    tail_visited = set([(0, 0)])

    with open('Day9/input.txt') as file:
        for line in file.readlines():
            dir, steps = parse_line(line)
            for _ in range(steps):
                knots[0] = move(knots[0], dir)
                for i in range(1, rope_size):
                    knots[i] = move_tail(knots[i], knots[i - 1])
                tail_visited.add(knots[-1])
    return len(tail_visited)


class ProblemTestCase(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(problem(2), 6266)

    def test_problem2(self):
        self.assertEqual(problem(10), 2369)


if __name__ == '__main__':
    unittest.main()
