def part1():
    suma =0
    file = open('data/input3.txt', 'r', encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        n = int(len(line) / 2)
        chunks = [line[i:i+n] for i in range(0, len(line), n)]
        characters_list = [[*chunks[0]], [*chunks[1]]]
        same_letter = next(iter(set(characters_list[0]).intersection(characters_list[1])))
        suma+=count_priority(same_letter)
    return suma

def count_priority(letter):
    v = ord(letter)
    if v>64 and v<91:
        return v-38
    elif v>96 and v<127:
        return v-96
    else:
        return 0

def part2():
    suma =0
    file = open('data/input3.txt', 'r', encoding="utf-8")
    lines = file.read().splitlines()
    for i in range (0, int(len(lines)), 3):
        subset = set(lines[i]).intersection(lines[i+1])
        result = next(iter(set(subset).intersection(lines[i+2])))
        suma+=count_priority(result)
    return suma