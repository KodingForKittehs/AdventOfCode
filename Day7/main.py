import unittest

class Directory:
    alldirs = []

    def __init__(self, name, parent=None):
        self.name = name
        self.size = 0
        self.parent = parent
        self.dirs = {}
        self.alldirs.append(self)


input = [line.strip() for line in open('Day7/input.txt').readlines()]
root_dir = Directory('/')
current = root_dir


def get_dir_size(dir):
    size = dir.size
    for subdir in dir.dirs.values():
        size += get_dir_size(subdir)
    return size


def problem1():
    total = 0
    for line in input:
        match line.split():
            case ['$', 'cd', '/']:
                current = root_dir
            case ['$', 'cd', '..']:
                current = current.parent
            case ['$', 'cd', dirname]:
                current = current.dirs[dirname]
            case ['$', 'ls']:
                pass
            case ['dir', dirname]:
                if dirname not in current.dirs:
                    current.dirs[dirname] = Directory(dirname, current)
            case [size, _]:
                current.size += int(size)
            case _:
                print(f"Unhandled: {line}")

    for dir in Directory.alldirs:
        dir_size = get_dir_size(dir)
        if dir_size <= 100000:
            total += dir_size

    return total


def problem2():
    sizes = []
    used_size = get_dir_size(root_dir)
    space_to_free = used_size - 40000000
    for dir in Directory.alldirs:
        sizes.append(get_dir_size(dir))
    sizes = list(sorted(sizes))
    for i, c in enumerate(sizes):
        if c > space_to_free:
            return sizes[i]


class ProblemTestCase(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(problem1(), 1543140)

    def test_problem2(self):
        self.assertEqual(problem2(), 1117448)


if __name__ == '__main__':
    unittest.main()
