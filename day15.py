def read_input():
    grid = []
    start = [0, 0]
    directions = []
    with open("inputs/day15.txt", "r") as f:
        line = f.readline().strip()
        while line != "":
            cur = []
            for i in range(len(line)):
                x = 0
                match line[i]:
                    case "O":
                        x = 1
                    case "#":
                        x = 2
                    case "@":
                        x = 3
                        start = [len(grid), i]
                cur.append(x)
            grid.append(cur)
            line = f.readline().strip()

        line = f.readline().strip()
        while line != "":
            for i in range(len(line)):
                x = 0
                match line[i]:
                    case "v":
                        x = 1
                    case ">":
                        x = 2
                    case "<":
                        x = 3
                directions.append(x)
            line = f.readline().strip()
    
    return grid, directions, start

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
    
def apply_dir(grid, dir, r, c, sr, sc):
    if grid[r][c] == 0:
        grid[r][c] = 1
        return True
    if grid[r][c] == 2:
        return False
    return apply_dir(grid, dir, r+dr[dir], c+dc[dir], sr, sc)
        
def compute_score(grid):
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                result += 100*r + c
    return result

def part1():
    grid, dirs, start = read_input()
    r = start[0]
    c = start[1]
    for dir in dirs:
        nr = r+dr[dir]
        nc = c+dc[dir]
        if apply_dir(grid, dir, nr, nc, r, c):
            grid[r][c] = 0
            grid[nr][nc] = 3
            r, c = nr, nc
    return compute_score(grid)
    

def part2():
    pass

if __name__ == "__main__":
    print(part1())
    print(part2())