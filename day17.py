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
    # print(f"performing op with a: {a} b: {b} c: {c} i: {i} [{ins[i]},{ins[i+1]}]")
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

def part2():
    init_a, init_b, init_c, ins = read_input()
    init_a = 0
    off = [1]
    oi = 0
    ans = part1().split(",")
    while(True):
        if init_a % 1000000 == 0:
            print(f"a: {init_a}")
        ri = 0
        i = 0
        a = init_a
        b = init_b
        c = init_c
        cache = set()
        while i < len(ins)-1:
            if (a, b, c, i) in cache:
                ri = 0
                break
            cache.add((a, b, c, i))
            a, b, c, i, res = perform_op(a, b, c, ins, i)
            if res != -1:
                if ri > len(ins) or ins[ri] != res:
                    break
                ri += 1
        if ri == len(ins):
            return init_a
        elif ri == 4:
            print(f"closer...{ri} {init_a}")
        init_a += off[oi]
        oi = (oi+1)%len(off)
    
print(part1())
print(part2())