import time
import copy

lines = open("inputs/day23.txt", "r").read().split("\n")
graph = [[0 for _ in range(26*26)] for _ in range(26*26)]

def translate(cc):
    res = ""
    cc.sort()
    for c in cc:
        res += chr(ord('a')+c//26) + chr(ord('a')+c%26) + ","
    return res

def cs(cp):
    return (ord(cp[0])-ord('a'))*26 + ord(cp[1]) - ord('a')

for line in lines:
    l = line.split("-")
    a = cs(l[0])
    b = cs(l[1])
    graph[a][b] = 1
    graph[b][a] = 1

left = (ord('t')-ord('a'))*26
right = left + 26

cur = []
p1 = 0
for i in range(len(graph)):
    for j in range(i+1, len(graph)):
        for k in range(j+1, len(graph)):
            if graph[i][j] == 1 and graph[i][k] == 1 and graph[j][k] == 1:
                cur.append([i, j, k])
                if (i >= left and i < right) or (j >= left and j < right) or (k >= left and k < right):
                    p1 += 1
print(f"p1: {p1}")


def validate(graph, g, i):
    for r in g:
        if graph[r][i] == 0:
            return False
    return True

best = 2
prev = cur
while len(cur) > 0:
    ng = []
    best += 1
    for g in cur:
        for i in range(g[-1]+1, len(graph)):
            if validate(graph, g, i):
                cg = copy.deepcopy(g)
                cg.append(i)
                ng.append(cg)
    prev = cur
    cur = ng

print(f"p2: {translate(prev[0])[:-1]}")