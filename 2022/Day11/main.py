import unittest
from collections import deque
import pathlib

input_file = f"{pathlib.Path(__file__).parent}/input.txt"
sample_file = f"{pathlib.Path(__file__).parent}/sample.txt"

class Monkey:
    lcm = 1
    def __init__(self):
        self.items = deque()
        self.operator = None
        self.divide = None
        self.if_true = None
        self.if_false = None
        self.count = 0


def problem(input, rounds, worry):
    monkeys = []
    with open(input) as file:
        for line in file:
            match line.split():
                case ['Monkey', _]:
                    monkeys.append(Monkey())
                case ['Starting', *_]:
                    nums = line.split(':')[1].split(',')
                    monkeys[-1].items = deque([int(item) for item in nums])
                case ['Operation:', *_]:
                    monkeys[-1].operator = line.split('=')[1].strip()
                case ['Test:', *_, val]:
                    monkeys[-1].divide = int(val)
                    Monkey.lcm *= int(val)
                case ['If', 'true:', *_, val]:
                    monkeys[-1].if_true = int(val)
                case ['If', 'false:', *_, val]:
                    monkeys[-1].if_false = int(val)

    for round in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                monkey.count += 1
                old = item
                item = eval(monkey.operator)
                if worry:
                    item = item // 3
                else:
                    item = item % Monkey.lcm
                if item % monkey.divide == 0:
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)
    sort = sorted(monkeys, key=lambda monkey: monkey.count, reverse=True)
    return sort[0].count * sort[1].count


class ProblemTestCase(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(problem(sample_file, 20, True), 10605)
        self.assertEqual(problem(input_file, 20, True), 98280)
        self.assertEqual(problem(sample_file, 10000, False), 2713310158)
        self.assertEqual(problem(input_file, 10000, False), 17673687232)


if __name__ == '__main__':
    unittest.main()
