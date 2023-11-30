import unittest

dirs = [
    (1, 0),
    (1, -1),
    (1, 1)
]

def add_line(grid, start_str, end_str):
    start = [int(i) for i in start_str.split(',')]
    end = [int(i) for i in end_str.split(',')]
    miny = min(start[1], end[1])
    maxy = max(start[1], end[1])
    minx = min(start[0], end[0])
    maxx = max(start[0], end[0])
    for i in range(miny, maxy + 1):
        for j in range(minx, maxx + 1):
            grid[(i, j)] = '#'


def get_bounds(grid_set):
    minj, maxj = 500, 500
    for coord in grid_set:
        minj = min(minj, coord[1])
        maxj = max(maxj, coord[1])
    return minj, maxj


def get_floor(grid_set):
    maxi = 0
    for coord in grid_set:
        maxi = max(maxi, coord[0])
    return maxi + 2


def get_grid(input):
    grid = {}
    with open(input) as file:
        for line in file.readlines():
            coords = [item.strip() for item in line.split('->')]
            for i in range(len(coords) - 1):
                start = coords[i]
                end = coords[i + 1]
                add_line(grid, start, end)
    return grid


def get_next(grid, bounds, floor, sand):
    for dir in dirs:
        to = (sand[0] + dir[0], sand[1] + dir[1])
        if bounds:
            if to[1] < bounds[0] or to[1] > bounds[1]:
                return None
        if floor and to[0] == floor:
            grid[sand] = 'o'
            return (0, 500)
        if to not in grid:
            return to
    grid[sand] = 'o'
    if sand == (0, 500):
        return None
    return (0, 500)


def problem1(input):
    grid = get_grid(input)
    bounds = get_bounds(grid)

    sand = (0, 500)
    while sand:
        sand = get_next(grid, bounds, None, sand)

    return list(grid.values()).count('o')


def problem2(input):
    grid = get_grid(input)
    floor = get_floor(grid)

    sand = (0, 500)
    while sand:
        sand = get_next(grid, None, floor, sand)

    return list(grid.values()).count('o')


class ProblemTestCase(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(problem1('Day14/sample1.txt'), 24)
        self.assertEqual(problem1('Day14/input1.txt'), 672)
        self.assertEqual(problem2('Day14/sample1.txt'), 93)
        self.assertEqual(problem2('Day14/input1.txt'), 26831)


if __name__ == '__main__':
    unittest.main()
