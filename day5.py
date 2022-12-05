def part1():
    file = open('data/input5.txt', 'r', encoding="utf-8")
    lines = file.readlines()
    crates_stack = prepare_crates_stack(lines)
    moves = prepare_moves(lines)
    for x in moves:
        amount = int(x[1])
        from_where = int(x[3])-1
        to_where = int(x[5])-1
        to_move = crates_stack[from_where][-amount:]
        crates_stack[from_where]=crates_stack[from_where][:len(crates_stack[from_where])-amount]
        for crate in to_move[::-1]:
            crates_stack[to_where]+=crate
    output=''
    for crate in crates_stack:
        output+=crate[-1]
    return output

def part2():
    file = open('data/input5.txt', 'r', encoding="utf-8")
    lines = file.readlines()
    crates_stack = prepare_crates_stack(lines)
    moves = prepare_moves(lines)
    for x in moves:
        amount = int(x[1])
        from_where = int(x[3])-1
        to_where = int(x[5])-1
        to_move = crates_stack[from_where][-amount:]
        crates_stack[from_where]=crates_stack[from_where][:len(crates_stack[from_where])-amount]
        crates_stack[to_where]+=to_move
    output=''
    for crate in crates_stack:
        output+=crate[-1]
    return output



def count_lines_of_crates(lines):
    count = 0
    while lines[count]!='\n':
        count+=1
    return count

def prepare_crates_stack(lines):
    cratesStack = []
    high_of_crates = count_lines_of_crates(lines)
    bottom_line = lines[high_of_crates-1].split()
    for i in range(len(bottom_line)):
        cratesStack.append([])
        cratesStack[i].append(bottom_line[i])

    for i in range(high_of_crates-1):
        for j in range(len(bottom_line)):
            cratesStack[j].append(lines[7-i][1+4*j])

    for i in range(len(bottom_line)-1):
        while ' ' in cratesStack[i]:cratesStack[i].remove(' ')
    return cratesStack

def prepare_moves(lines):
    moves = []
    for i in range(count_lines_of_crates(lines)+1, len(lines)):
        moves.append(lines[i].split())
    return moves
