def read_input():
    pts = []
    with open("inputs/day18.txt", "r") as f:
        line = f.readline().strip()
        while line != "":
            pt = [int(i) for i in line.split(",")]
            pts.append(pt)
            line = f.readline().strip()
    return pts

def print_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            print(str(grid[r][c]) + " ", end="")
        print("")

def simulate(pts, falling=1024):
    grid = [[float('inf') for _ in range(71)] for _ in range(71)]
    for i in range(falling):
        grid[pts[i][0]][pts[i][1]] = -1
    grid[0][0] = 0

    q = [[0, 0]]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while len(q) > 0:
        r, c  = q.pop(0)
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if nr == 70 and nc == 70:
                return grid[r][c]+1
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid):
                continue
            if grid[nr][nc] == float('inf'):
                grid[nr][nc] = grid[r][c]+1
                q.append((nr, nc))
    return -1

pts = read_input()

print(f"p1: {simulate(pts)}")

for i in range(1025, len(pts)):
    if simulate(pts, i) == -1:
        print(f"p2: {pts[i-1]}")
        break