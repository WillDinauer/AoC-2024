import copy

def read_input():
    with open("inputs/day20.txt", "r") as f:
        grid = []
        line = f.readline().strip()
        while line != "":
            cur = []
            for i in range(len(line)):
                if line[i] == "#":
                    cur.append(-1)
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

def fill_grid(grid, start, end = [-1, -1]):
    visited = set()
    
    q = [(start[0], start[1], 0)]
    result = 0
    while len(q) > 0:
        r, c, t = q.pop(0)
        if [r, c] == end:
            result = t
        visited.add((r, c))
        grid[r][c] = t
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if grid[nr][nc] == 0 and (nr, nc) not in visited:
                q.append((nr, nc, t+1))
    return result

grid, start, end = read_input()
ge = copy.deepcopy(grid)
base = fill_grid(grid, start, end)
fill_grid(ge, end)

def search(grid, ge, base, cheat):
    result = 0
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):
            if grid[r][c] != -1:
                for er in range(max(1, r-cheat), min(len(grid)-2, r+cheat)+1):
                    for ec in range(max(1, c-cheat+abs(r-er)), min(len(grid[0])-2, c+cheat-abs(r-er))+1):
                        if grid[er][ec] != -1 and base - (grid[r][c] + abs(er-r) + abs(ec-c) + ge[er][ec]) >= 100:
                            result += 1
    return result

print(f"p1: {search(grid, ge, base, 2)}")
print(f"p2: {search(grid, ge, base, 20)}")
