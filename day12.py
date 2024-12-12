def read_grid():
    with open("inputs/day12.txt", "r") as f:
        grid = []
        line = f.readline().strip()
        while line != "":
            grid.append(line)
            line = f.readline().strip()
        return grid
    
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(grid, v, r, c, val, p):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != val:
        return 0, 1
    if v[r][c] == 1:
        return 0, 0
    v[r][c] = 1
    area = 1
    perimeter = 0
    for i in range(4):
        sa, sp = dfs(grid, v, r+dr[i], c+dc[i], val, p)
        area += sa
        perimeter += sp
    return area, perimeter

def compute_region(grid, v, r, c):
    val = grid[r][c]
    perimeter = []
    area, perimeter = dfs(grid, v, r, c, val, perimeter)
    return area * perimeter

def part1():
    grid = read_grid()
    v = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if v[r][c] == 0:
                result += compute_region(grid, v, r, c)
    return result

def part2():
    pass

if __name__ == "__main__":
    print(part1())
    print(part2())