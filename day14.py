def read_input():
    p = []
    v = []
    with open("inputs/day14.txt", "r") as f:
        line = f.readline().strip()
        while line != "":
            coords = line.split()[0].split("=")[1].split(",")
            p.append([int(coords[0]), int(coords[1])])

            coords = line.split()[1].split("=")[1].split(",")
            v.append([int(coords[0]), int(coords[1])])
            line = f.readline().strip()
    return p, v

def handle_bot(p, v):
    p[0] = (p[0] + v[0]*100)%101
    p[1] = (p[1] + v[1]*100)%103
    if p[0] > 50:
        if p[1] > 51:
            return 0
        elif p[1] < 51:
            return 1
    elif p[0] < 50:
        if p[1] > 51:
            return 2
        elif p[1] < 51:
            return 3
    return 4

def part1():
    p, v = read_input()
    quads = [0]*5
    for i in range(len(p)):
        quads[(handle_bot(p[i], v[i]))] += 1
    return quads[0]*quads[1]*quads[2]*quads[3]

def part2():
    pass

if __name__ == "__main__":
    print(part1())
    print(part2())