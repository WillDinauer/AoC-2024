def read_input():
    nodes = {}
    with open("inputs/day8.txt", "r") as f:
        line = f.readline().strip()
        r = 0
        m = len(line)
        while line != "":
            for i in range(len(line)):
                if line[i] != ".":
                    if line[i] not in nodes:
                        nodes[line[i]] = []
                    nodes[line[i]].append([r, i])
            r += 1
            line = f.readline().strip()
    grid = [[0 for _ in range(m)] for _ in range(r)]
    return nodes, grid

def fill_grid(p1, p2, grid):
    r1 = 2*p1[0]-p2[0]
    c1 = 2*p1[1]-p2[1]

    r2 = 2*p2[0]-p1[0]
    c2 = 2*p2[1]-p1[1]
    
    res = 0
    if r1 >= 0 and r1 < len(grid) and c1 >= 0 and c1 < len(grid[0]) and grid[r1][c1] == 0:
        grid[r1][c1] = 1
        res += 1
    if r2 >= 0 and r2 < len(grid) and c2 >= 0 and c2 < len(grid[0]) and grid[r2][c2] == 0:
        grid[r2][c2] = 1
        res += 1
    return res


def part1():
    nodes, grid = read_input()
    result = 0
    for freq in nodes:
        positions = nodes[freq]
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                result += fill_grid(positions[i], positions[j], grid)
    return result
    

def part2():
    nodes, grid = read_input()

if __name__ == "__main__":
    print(part1())
    print(part2())