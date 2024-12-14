import time

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
    p, v = read_input()
    t = 7916

    # This was in a loop until I found the solution
    grid = [["." for _ in range(101)] for _ in range(103)]
    for i in range(len(p)):
        grid[(p[i][1]+v[i][1]*t)%103][(p[i][0]+v[i][0]*t)%101] = "#"
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            print(grid[r][c], end="")
        print()
    print(f"Elapsed time: {t}\n\n")
    time.sleep(1)
    t += 103

if __name__ == "__main__":
    print(part1())
    part2()