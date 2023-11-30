import unittest
from collections import deque
import pathlib

input_file = f"{pathlib.Path(__file__).parent}/input.txt"
sample_file = f"{pathlib.Path(__file__).parent}/sample.txt"

def start_end(grid):
    for i, ic in enumerate(grid):
        for j, jc in enumerate(ic):
            if jc == 'S':
                start = i, j
            if jc == 'E':
                end = i, j
    return start, end


dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


def in_bounds(grid, coord):
    return (
        coord[0] < len(grid) and coord[0] >= 0
        and coord[1] < len(grid[0]) and coord[1] >= 0
    )


def can_travel(grid, src, dst):
    src_char = grid[src[0]][src[1]]
    dst_char = grid[dst[0]][dst[1]]

    if dst_char == 'E':
        return src_char in 'yz'

    res = ord(dst_char) <= (ord(src_char) + 1)
    return res


def problem(input, user_start=None):
    with open(input) as file:
        grid = [line.strip() for line in file.readlines()]

    start, end = start_end(grid)
    grid[start[0]] = grid[start[0]].replace('S', 'a')

    if user_start:
        visited = {user_start: 0}
        current = deque([user_start])
    else:
        visited = {start: 0}
        current = deque([start])

    while current:
        node = current.popleft()
        if grid[node[0]][node[1]] == 'E':
            return visited[node]
        for dir in dirs:
            nxt = node[0] + dir[0], node[1] + dir[1]
            if not in_bounds(grid, nxt):
                continue
            if (
                nxt not in visited
                and can_travel(grid, node, nxt)
            ):
                visited[nxt] = visited[node] + 1
                current.append(nxt)
            pass
    return 10000

def problem2(input, user_start=None):
    with open(input) as file:
        grid = [line.strip() for line in file.readlines()]
    mn = 1000
    for i, ic in enumerate(grid):
        for j, jc in enumerate(ic):
            if jc in 'aS':
                mn = min(mn, problem(input, (i, j)))
    return mn


class ProblemTestCase(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(problem(sample_file), 31)
        self.assertEqual(problem(input_file), 425)
        self.assertEqual(problem2(input_file), 418)


if __name__ == '__main__':
    unittest.main()
