def convert_line(line, grid, starting_pos):
    cur = []
    for i in range(len(line)):
        match line[i]:
            case ".":
                cur.append(0)
            case "#":
                cur.append(1)
            case "^":
                cur.append(0)
                starting_pos = [len(grid), i]
    return cur, starting_pos

def read_grid():
    grid = []
    starting_pos = []
    with open("inputs/day6.txt", "r") as f:
        line = f.readline()
        while line != "":
            cur, starting_pos = convert_line(line, grid, starting_pos)
            grid.append(cur)
            line = f.readline()
    return grid, starting_pos


def part1():
    grid, starting_pos = read_grid()
    result = find_positions(grid, starting_pos)
    return len(result)

def find_positions(grid, starting_pos):
    # Step helpers
    diff_r = [-1, 0, 1, 0]
    diff_c = [0, 1, 0, -1]
    idx = 0     # (moving up to start)

    # Initial position and result
    mr = starting_pos[0]
    mc = starting_pos[1]
    result = []

    while (True):
        # Check for previously unoccupied spaces
        if grid[mr][mc] == 0:
            result.append([mr, mc])
            grid[mr][mc] = 2

        # 'Potential' r/c -> Where we will be moving to
        pr = mr + diff_r[idx]
        pc = mc + diff_c[idx]

        # Check if we are leaving the grid
        if pc < 0 or pr < 0 or pr >= len(grid) or pc >= len(grid[0]):
            return result
        
        # Are we hitting an obstacle? Rotate
        if (grid[pr][pc] == 1):
            idx = (idx + 1) % 4
        else:       
            # Otherwise, take a step
            mr = pr
            mc = pc

def try_grid(grid, starting_pos):
    # Initial r and c
    mr = starting_pos[0]
    mc = starting_pos[1]

    # Step helpers
    diff_r = [-1, 0, 1, 0]
    diff_c = [0, 1, 0, -1]
    idx = 0     # (moving up to start)

    seen = [[] for _ in range(4)]

    while (True):
        # Check if we've already been here before (same position, same direction)
        if [mr, mc] in seen[idx]:
            return 1
        seen[idx].append([mr, mc])
        
         # 'Potential' r/c -> Where we will be moving to
        pr = mr + diff_r[idx]
        pc = mc + diff_c[idx]

        # Check if we are leaving the grid...if so, we failed to trap the guard.
        if pc < 0 or pr < 0 or pr >= len(grid) or pc >= len(grid[0]):
            return 0
        
        # Are we hitting an obstacle? Rotate
        if (grid[pr][pc] == 1):
            idx = (idx + 1) % 4
        else:       
            # Otherwise, take a step
            mr = pr
            mc = pc
        

def part2():
    grid, starting_pos = read_grid()

    positions = find_positions(grid, starting_pos)

    # reset grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                grid[r][c] = 0

    result = 0
    # Try all interferring positions
    for idx, pos in enumerate(positions):
        if (idx % 100 == 0):
            print(f"Processing position {idx}/{len(positions)}")
        if pos != starting_pos:
            grid[pos[0]][pos[1]] = 1
            result += try_grid(grid, starting_pos)
            grid[pos[0]][pos[1]] = 0
    return result
    
if __name__ == "__main__":
    print(part1())
    print(part2())