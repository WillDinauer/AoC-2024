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

def print_grid(grid, path):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            print("O" if [r, c] in path else grid[r][c], end="")
        print()

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

if __name__ == "__main__":
    grid, start, end = read_input()
    score = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited = set()
    prev = {}
    q = []
    heapq.heapify(q)
    heapq.heappush(q, [0, start[0], start[1], 1, None])
    p1 = -1
    while len(q) > 0:
        cur, r, c, dir, p = heapq.heappop(q)
        if (r, c, dir) in visited:
            if cur == score[r][c] and p not in prev[node]:
                prev[node].append(p)
            continue

        node = (cur, r, c)
        if node not in prev:
            prev[node] = []
        prev[node].append(p)

        if [r, c] == end and p1 < 0:
            p1 = cur
        
        visited.add((r, c, dir))
        score[r][c] = cur
        nr = r + dr[dir]
        nc = c + dc[dir]
        if grid[nr][nc] == "." or grid[nr][nc] == "E":
            heapq.heappush(q, [cur+1, nr, nc, dir, node])

        for rotation in [-1, 1]:
            heapq.heappush(q, [cur + 1000, r, c, (dir + rotation)%4, node])

    cur = [(p1, end[0], end[1])]
    seen = []
    path = []
    while len(cur) > 0:
        new_cur = []
        for pt in cur:
            if pt == None:
                break
            if pt not in seen:
                seen.append(pt)
                if [pt[1], pt[2]] not in path:
                    path.append([pt[1], pt[2]])
                for np in prev[pt]:
                    new_cur.append(np)
        cur = new_cur
    print_grid(grid, path)

    print(f"p1: {p1}")
    print(f"p2: {len(path)}")