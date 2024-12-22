nums = [int(i) for i in open("inputs/day22.txt", "r").read().split("\n")]

mn = 16777216
def apply(n):
    n = (n ^ (n << 6)) % mn
    n = (n ^ (n >> 5)) % mn
    n = (n ^ (n << 11)) % mn
    return n

s = 19

g = [[[[0 for _ in range(s)] for _ in range(s)] for _ in range(s)] for _ in range(s)]

p1 = 0
for n in nums:
    d = []
    seen = set()
    for _ in range(2000):
        p = apply(n)
        d.append((p%10)-(n%10) + 9)
        if len(d) == 5:
            d.pop(0)
        if len(d) == 4 and tuple(d) not in seen:
            g[d[0]][d[1]][d[2]][d[3]] += p%10
            seen.add(tuple(d))
        n = p
    p1 += n
print(f"p1: {p1}")

p2 = 0
for a in range(s):
    for b in range(s):
        for c in range(s):
            for d in range(s):
                p2 = max(p2, g[a][b][c][d])
print(f"p2: {p2}")