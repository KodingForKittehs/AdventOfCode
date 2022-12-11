import unittest
from collections import deque

class Monkey:
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
                case ['If', 'true:', *_, val]:
                    monkeys[-1].if_true = int(val)
                case ['If', 'false:', *_, val]:
                    monkeys[-1].if_false = int(val)

    for round in range(rounds):
        print(round)
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                monkey.count += 1
                old = item
                item = eval(monkey.operator)
                print(item)
                if worry:
                    item = item // 3
                if item % monkey.divide == 0:
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)
    sort = sorted(monkeys, key=lambda monkey: monkey.count, reverse=True)
    return sort[0].count * sort[1].count


class ProblemTestCase(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(problem('Day11/sample1.txt', 20, True), 10605)
        self.assertEqual(problem('Day11/input1.txt', 20, True), 98280)
        #self.assertEqual(problem('Day11/sample1.txt', 10000, False), 2713310158)


if __name__ == '__main__':
    unittest.main()
