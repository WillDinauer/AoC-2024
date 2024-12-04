def create_grid():
    # Read in the inputs
    with open("inputs/day4.txt", "r") as f:
        return f.readlines()
    
def helper(grid, r, c, dr, dc, i):
    # Bounds checking 
    if r<0 or c<0 or r>=len(grid) or c>=len(grid[r]):
        return 0
    
    # 'i' used to orient us in the sequence (M=1,A=2,S=3)
    if i == 1:
        if grid[r][c] != "M":
            return 0
        else:
            return helper(grid, r+dr, c+dc, dr, dc, 2)
    elif i == 2:
        if grid[r][c] != "A":
            return 0
        else:
            return helper(grid, r+dr, c+dc, dr, dc, 3)
    elif i == 3:
        return 1 if grid[r][c] == "S" else 0
    
def search_xmas(grid, r, c):
    diff = [-1, 0, 1]
    result = 0
    # Search for "MAS" in all directions
    # (even if dr==0 && dc==0, helper returns 0)
    for dr in diff:
        for dc in diff:
            result += helper(grid, r+dr, c+dc, dr, dc, 1)
    return result
    
def part1():
    grid = create_grid()
    result = 0
    # Search for X's to find XMAS
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "X":
                result += search_xmas(grid, r, c)
    return result

def search_cross(grid, r, c):
    # Look for MAS and MAS in an X-formation
    num_s = 0
    num_m = 0
    diff = [-1, 1]
    for dr in diff:
        for dc in diff:
            if grid[r+dr][c+dc] == "S":
                num_s += 1
            elif grid[r+dr][c+dc] == "M":
                num_m += 1
            else:
                return 0
    # Check for 2 S, 2 M, and S/M must not be diagonally across from each other
    if num_s == 2 and num_m == 2 and grid[r-1][c-1] != grid[r+1][c+1]:
        return 1
    return 0

def part2():
    grid = create_grid()
    result = 0
    # Search for A's to find X-MAS...decreasing search bounds to rid of bounds checking
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[r])-1):
            if grid[r][c] == "A":
                result += search_cross(grid, r, c)
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())