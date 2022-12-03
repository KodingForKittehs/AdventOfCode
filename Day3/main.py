file = 'Day3/input.txt'
input = [line.strip() for line in open(file).readlines()]


def priority(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def problem_1():
    result = 0
    for line in input:
        s = set()
        for i, c in enumerate(line):
            if i < (len(line) // 2):
                s.add(c)
            else:
                if c in s:
                    result += priority(c)
                    break
    return result


def problem_2():
    result = 0
    for bags in chunks(input, 3):
        for c in bags[0]:
            if c in bags[1] and c in bags[2]:
                result += priority(c)
                break
    return result


if __name__ == "__main__":
    print(f'Part 1 solution: {problem_1()}')
    print(f'Part 2 solution: {problem_2()}')
