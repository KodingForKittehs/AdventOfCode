import unittest

def instruction_generator(input):
    with open(input) as file:
        for line in file.readlines():
            yield line.split()


def should_sum(n):
    return (n % 40 - 20) == 0


def problem(input):
    counter = 1
    x = 1
    sum = 0
    instructions = instruction_generator(input)
    task = None
    crt = ['']
    crt_width = 40

    while True:
        if should_sum(counter):
            sum += counter * x

        if abs(counter % 40 - 1 - x) <= 1:
            crt[len(crt) - 1] += '#'
        else:
            crt[len(crt) - 1] += '.'
        if len(crt[len(crt) - 1]) == crt_width:
            crt.append('')

        if task:
            x += int(task[1])
            task = None
        else:
            try:
                instruction = next(instructions)
            except StopIteration:
                for line in crt:
                    print(line)
                return sum, crt
            match instruction:
                case ['addx', _]:
                    task = instruction
                case ['noop']:
                    pass
        counter += 1

class ProblemTestCase(unittest.TestCase):

    def test_should_log(self):
        self.assertEqual(should_sum(20), True)
        self.assertEqual(should_sum(21), False)
        self.assertEqual(should_sum(40), False)
        self.assertEqual(should_sum(60), True)

    def test_sample1(self):
        self.assertEqual(problem('Day10/sample1.txt')[0], 13140)

    def test_input1(self):
        res = problem('Day10/input1.txt')
        self.assertEqual(res[0], 12520)

        expected_crt = [
            '####.#..#.###..####.###....##..##..#....',
            '#....#..#.#..#....#.#..#....#.#..#.#...#',
            '###..####.#..#...#..#..#....#.#....#...#',
            '#....#..#.###...#...###.....#.#.##.#...#',
            '#....#..#.#....#....#....#..#.#..#.#....',
            '####.#..#.#....####.#.....##...###.####.',
            '.'
        ]

        self.assertEqual(res[1], expected_crt)


if __name__ == '__main__':
    unittest.main()
