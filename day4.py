def part1():
    suma =0
    file = open('data/input4.txt', 'r', encoding="utf-8")
    lines = file.read().splitlines()
    for line in lines:
        r = line.replace('-', ',').split(sep=',')
        if is_overlap_completely(r):
            suma+=1
    return suma

def is_overlap_completely(r):
    if int(r[0]) >= int(r[2]) and int(r[1]) <= int(r[3]):
        return True
    elif int(r[2]) >= int(r[0]) and int(r[3]) <= int(r[1]):
        return True
    else:
        return False

def part2():
    suma =0
    file = open('data/input4.txt', 'r', encoding="utf-8")
    lines = file.read().splitlines()
    for line in lines:
        r = line.replace('-', ',').split(sep=',')
        if is_overlap(r):
            suma+=1
    return suma

def is_overlap(r):
    if int(r[0]) <= int(r[2]) <= int(r[1]) or int(r[0]) <= int(r[3]) <= int(r[1]):
        return True
    elif int(r[2]) <= int(r[0]) <= int(r[3]) or int(r[2]) <= int(r[1]) <= int(r[3]):
        return True
    else:
        return False