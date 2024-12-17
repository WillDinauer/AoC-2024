def read_input():
    with open("inputs/day17.txt", "r") as f:
        a = int(f.readline().strip().split()[2])
        b = int(f.readline().strip().split()[2])
        c = int(f.readline().strip().split()[2])
        f.readline()
        line = f.readline().strip().split()[1].split(",")
        ins = [int(i) for i in line]

        return a, b, c, ins

def perform_op(a, b, c, ins, i):
    match ins[i+1]:
        case 0 | 1 | 2 | 3:
            combo = ins[i+1]
        case 4:
            combo = a
        case 5:
            combo = b
        case 6:
            combo = c

    res = -1
    jumped = False
    match ins[i]:
        case 0:
            a = a//(2**combo)
        case 1:
            b = b ^ ins[i+1]
        case 2:
            b = combo % 8
        case 3:
            if a != 0:
                i = ins[i+1]
                jumped = True
        case 4:
            b = b ^ c
        case 5:
            res = combo%8
        case 6:
            b = a//(2**combo)
        case 7:
            c = a//(2**combo)

    if not jumped:
        i += 2
    return a, b, c, i, res


def part1():
    a, b, c, ins = read_input()
    i = 0
    result = ""
    while i < len(ins)-1:
        a, b, c, i, res = perform_op(a, b, c, ins, i)
        if res != -1:
            result += ","+str(res)
    return result[1:]

def backtrack(a, b, c, ins, ri):
    if ri < 0:
        return a
    a = a << 3
    for x in range(8):
        ta = a + x
        tb = b
        tc = c
        i = 0
        while i < len(ins)-1:
            ta, tb, tc, i, res = perform_op(ta, tb, tc, ins, i)
            if res != -1:
                if res == ins[ri]:
                    cont = backtrack(a + x, tb, tc, ins, ri-1)
                    if cont > 0:
                        return cont
                else:
                    break
    return -1


def part2():
    a, b, c, ins = read_input()
    ri = len(ins)-1
    a = backtrack(0, b, c, ins, ri)
    return a
    
print(part1())
print(part2())