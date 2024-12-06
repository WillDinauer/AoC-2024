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

    # Step helpers
    diff_r = [-1, 0, 1, 0]
    diff_c = [0, 1, 0, -1]
    idx = 0     # (moving up to start)

    # Initial position and result
    mr = starting_pos[0]
    mc = starting_pos[1]
    result = 0

    while (True):
        # Check for previously unoccupied spaces
        if (grid[mr][mc] == 0):
            result += 1
            grid[mr][mc] = 2

        # 'Potential' r/c -> Where we will be moving to
        pr = mr + diff_r[idx]
        pc = mc + diff_c[idx]

        # Check if we are leaving the grid
        if (pc < 0 or pr < 0 or pr >= len(grid) or pc >= len(grid[0])):
            return result
        
        # Are we hitting an obstacle? Rotate
        if (grid[pr][pc] == 1):
            idx = (idx + 1) % 4
        else:       
            # Otherwise, take a step
            mr = pr
            mc = pc
    
if __name__ == "__main__":
    print(part1())