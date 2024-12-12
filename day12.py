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

def dfs_p1(grid, v, r, c, val):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != val:
        return 0, 1
    if v[r][c] == 1:
        return 0, 0
    v[r][c] = 1
    area = 1
    perimeter = 0
    for i in range(4):
        sa, sp = dfs_p1(grid, v, r+dr[i], c+dc[i], val)
        area += sa
        perimeter += sp
    return area, perimeter

def compute_region(grid, v, r, c):
    val = grid[r][c]
    area, perimeter = dfs_p1(grid, v, r, c, val)
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


def dfs_p2(grid, v, r, c, val, cache, dir):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != val:
        if dir == 0 or dir == 1:
            cache[dir].append([r, c])
        else:
            cache[dir].append([c, r])
        return 0
    if v[r][c] == 1:
        return 0
    v[r][c] = 1
    area = 1
    for i in range(4):
        area += dfs_p2(grid, v, r+dr[i], c+dc[i], val, cache, i)
    return area

def compute_sides(cache):
    sides = 0
    for direction in cache:
        sides += 1
        line = cache[direction]
        line.sort()
        for i in range(len(line)-1):
            if line[i+1][0] != line[i][0]:
                sides += 1
            elif line[i+1][1] > line[i][1] + 1:
                sides += 1
    return sides

def side_finder(grid, v, r, c):
    cache = {0:[], 1:[], 2:[], 3:[]}
    val = grid[r][c]
    area = dfs_p2(grid, v, r, c, val, cache, -1)
    sides = compute_sides(cache)
    return area * sides

def part2():
    grid = read_grid()
    v = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if v[r][c] == 0:
                result += side_finder(grid, v, r, c)
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())