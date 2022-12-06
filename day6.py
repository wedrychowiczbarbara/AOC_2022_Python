def part1():
    file = open('data/input6.txt', 'r', encoding="utf-8")
    data = file.read()
    for i in range(0, len(data) - 4):
        input = data[i:i + 4]
        if len(set(filter(lambda x: input.count(x) >= 2, input))) > 0:
            continue
        else:
            return i + 4


def part2():
    n = 14
    file = open('data/input6.txt', 'r', encoding="utf-8")
    data = file.read()
    for i in range(0, len(data) - n):
        input = data[i:i + n]
        if len(set(filter(lambda x: input.count(x) >= 2, input))) > 0:
            continue
        else:
            return i + n
