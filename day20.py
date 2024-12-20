def read_input():
    with open("inputs/day20.txt", "r") as f:
        grid = []
        line = f.readline().strip()
        while line != "":
            cur = []
            for i in range(len(line)):
                if line[i] == "#":
                    cur.append(1)
                    continue
                elif line[i] == "S":
                    start = [len(grid), i]
                elif line[i] == "E":
                    end = [len(grid), i]
                cur.append(0)
            grid.append(cur)
            line = f.readline().strip()
        return grid, start, end

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_shortest(grid, start, end):
    visited = set()
    
    q = [(start[0], start[1], 0)]
    while len(q) > 0:
        r, c, t = q.pop(0)
        if r == end[0] and c == end[1]:
            return t
        visited.add((r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if grid[nr][nc] == 0 and (nr, nc) not in visited:
                q.append((nr, nc, t+1))
    return -1

grid, start, end = read_input()
base = find_shortest(grid, start, end)
cheats = 0
for r in range(1, len(grid)-1):
    print(f"On row: {r}/{len(grid)}")
    for c in range(1, len(grid[0])-1):
        if grid[r][c] == 1:
            grid[r][c] = 0
            if base - find_shortest(grid, start, end) >= 100:
                cheats += 1
            grid[r][c] = 1

print(f"p1: {cheats}")
            