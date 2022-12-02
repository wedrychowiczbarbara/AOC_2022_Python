def part1():
    max=0
    sum=0
    file = open('data/input1.txt', 'r', encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        if line.strip() != '':
            num = int(line.strip())
            sum+=num
        else:
            if sum>max:
                max=sum
            sum=0
    file.close()
    return max


def part2():
    max_three=[0, 0, 0]
    suma=0
    file = open('data/input1.txt', 'r', encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        if line.strip() != '':
            num = int(line.strip())
            suma+=num
        else:
            if any(i<suma for i in max_three):
                max_three.append(suma)
                max_three.sort(reverse=True)
                max_three = max_three[:-1]
            suma=0
    file.close()
    return sum(max_three)