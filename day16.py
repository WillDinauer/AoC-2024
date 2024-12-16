import heapq

def read_input():
    with open("inputs/day16.txt", "r") as f:
        grid = []
        line = f.readline().strip()
        while line != "":
            for i in range(len(line)):
                if line[i] == "S":
                    start = [len(grid), i]
                elif line[i] == "E":
                    end = [len(grid), i]
            grid.append(line)
            line = f.readline().strip()
        return grid, start, end

def print_grid(grid, start, end, prev):
    path = []
    cur = prev[end[0], end[1]]
    while cur != start:
        path.append(cur)
        cur = prev[cur[0], cur[1]]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            print("X" if [r, c] in path else grid[r][c], end="")
        print()


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def part1():
    grid, start, end = read_input()
    visited = set()
    q = []
    heapq.heapify(q)
    heapq.heappush(q, [0, start[0], start[1], 1])
    while len(q) > 0:
        cur, r, c, dir = heapq.heappop(q)
        if (r, c, dir) in visited:
            continue
        
        if [r, c] == end:
            return cur
        
        visited.add((r, c, dir))
        nr = r + dr[dir]
        nc = c + dc[dir]
        if grid[nr][nc] == "." or grid[nr][nc] == "E":
            heapq.heappush(q, [cur+1, nr, nc, dir])

        for rotation in [-1, 1]:
            heapq.heappush(q, [cur + 1000, r, c, (dir + rotation)%4])

    return float('inf')
            
def part2():
    pass

if __name__ == "__main__":
    print(part1())
    print(part2())