import time

def print_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            match grid[r][c]:
                case 0:
                    character = "."
                case 1:
                    character = "O"
                case 2:
                    character = "#"
                case 3:
                    character = "@"
                case 4:
                    character = "["
                case 5:
                    character = "]"
            print(character, end="")
        print()
    print("\n")

def read_input(scale=False):
    grid = []
    start = [0, 0]
    directions = []
    with open("inputs/day15.txt", "r") as f:
        line = f.readline().strip()
        while line != "":
            cur = []
            for i in range(len(line)):
                match line[i]:
                    case ".":
                        cur.append(0)
                        if scale:
                            cur.append(0)
                    case "O":
                        if scale:
                            cur.append(4)
                            cur.append(5)
                        else:
                            cur.append(1)
                    case "#":
                        cur.append(2)
                        if scale:
                            cur.append(2)
                    case "@":
                        cur.append(3)
                        start = [len(grid), i]
                        if scale:
                            cur .append(0)
                            start = [len(grid), i*2]
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
    
def apply_dir(grid, dir, r, c):
    if grid[r][c] == 0:
        grid[r][c] = grid[r-dr[dir]][c-dc[dir]]
        return True
    if grid[r][c] == 2:
        return False
    
    if apply_dir(grid, dir, r+dr[dir], c+dc[dir]):
        grid[r][c] = grid[r-dr[dir]][c-dc[dir]]
        return True
    return False
        
def compute_score(grid):
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1 or grid[r][c] == 4:
                result += 100*r + c
    return result

def consider(cur, p):
    if p not in cur:
        cur.append(p)

def handle_box(cur, np, offset):
    consider(cur, np)
    consider(cur, [np[0], np[1]+offset])

def apply_dir2(grid, dir, prev):
    np = []
    cur = []
    for pos in prev:
        np = [pos[0]+dr[dir], pos[1]+dc[dir]]
        match grid[np[0]][np[1]]:
            case 2:
                return False
            case 4:
                handle_box(cur, np, 1)
            case 5:
                handle_box(cur, np, -1)
    
    if len(cur) == 0 or apply_dir2(grid, dir, cur):
        for p in prev:
            grid[p[0]+dr[dir]][p[1]+dc[dir]] = grid[p[0]][p[1]]
            grid[p[0]][p[1]] = 0
        return True
    return False

def apply_moves(scale=False):
    grid, dirs, start = read_input(scale)
    r = start[0]
    c = start[1]
    for dir in dirs:
        nr = r+dr[dir]
        nc = c+dc[dir]
        if ((not scale or dir == 2 or dir == 3) and apply_dir(grid, dir, nr, nc)) or (scale and apply_dir2(grid, dir, [[r, c]])):
            grid[r][c] = 0
            r, c = nr, nc
    return compute_score(grid)

def part1():
    return apply_moves()
    
def part2():
    return apply_moves(True)

if __name__ == "__main__":
    print(part1())
    print(part2())