lines = open("inputs/day23.txt", "r").read().split("\n")
graph = [[0 for _ in range(26*26)] for _ in range(26*26)]

def cs(cp):
    return (ord(cp[0])-ord('a'))*26 + ord(cp[1]) - ord('a')

for line in lines:
    l = line.split("-")
    a = cs(l[0])
    b = cs(l[1])
    graph[a][b] = 1
    graph[b][a] = 1

tl = (ord('t')-ord('a'))*26
tr = tl + 26
p1 = 0
seen = set()
for i in range(tl, tr):
    for j in range(len(graph)):
        for k in range(len(graph)):
            cur = [i, j, k]
            cur.sort()
            if not tuple(cur) in seen and graph[i][j] == 1 and graph[i][k] == 1 and graph[j][k] == 1:
                p1 += 1
                seen.add(tuple(cur))
print(f"p1: {p1}")