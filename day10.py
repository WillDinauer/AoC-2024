def read_grid():
    grid = []
    with open("inputs/day10.txt", "r") as f:
        line = f.readline().strip()
        while line != "":
            grid.append([int(line[i]) for i in range(len(line))])
            line = f.readline().strip()
    return grid

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def travel(grid, r, c, cur, res):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid) or grid[r][c] != cur:
        return
    if cur == 9:
        if [r, c] not in res:
            res.append([r, c])
        return
    temp = grid[r][c]
    grid[r][c] = -1
    for i in range(4):
        travel(grid, r+dr[i], c+dc[i], cur+1, res)
    grid[r][c] = temp
    return len(res)

def part1():
    grid = read_grid()
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                result += travel(grid, r, c, 0, [])
    return result

def new_rating(grid, r, c, cur):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid) or grid[r][c] != cur:
        return 0
    if cur == 9:
        return 1
    temp = grid[r][c]
    grid[r][c] = -1
    res = 0
    for i in range(4):
        res += new_rating(grid, r+dr[i], c+dc[i], cur+1)
    grid[r][c] = temp
    return res

def part2():
    grid = read_grid()
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                result += new_rating(grid, r, c, 0)
    return result
    
if __name__ == "__main__":
    print(part1())
    print(part2())