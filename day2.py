game_rules_1 = [
[['A', 'X'], 3, 1],
[['A', 'Y'], 6, 2],
[['A', 'Z'], 0, 3],
[['B', 'X'], 0, 1],
[['B', 'Y'], 3, 2],
[['B', 'Z'], 6, 3],
[['C', 'X'], 6, 1],
[['C', 'Y'], 0, 2],
[['C', 'Z'], 3, 3],
]

def part1():
    suma =0
    file = open('data/input2.txt', 'r', encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        data = line.split()
        for i in game_rules_1:
            if i[0] == data:
                suma=suma+i[1]+i[2]
    return suma

game_rules_2 = [
[['A', 'X'], 0, 3],
[['B', 'X'], 0, 1],
[['C', 'X'], 0, 2],
[['A', 'Y'], 3, 1],
[['B', 'Y'], 3, 2],
[['C', 'Y'], 3, 3],
[['A', 'Z'], 6, 2],
[['B', 'Z'], 6, 3],
[['C', 'Z'], 6, 1],
]

def part2():
    suma =0
    file = open('data/input2.txt', 'r', encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        data = line.split()
        for i in game_rules_2:
            if i[0] == data:
                suma=suma+i[1]+i[2]
    return suma
