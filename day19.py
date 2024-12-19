def read_input():
    with open("inputs/day19.txt", "r") as f:
        patterns = []
        towels = f.readline().strip().split(", ")
        f.readline()
        line = f.readline().strip()
        while line != "":
            patterns.append(line)
            line = f.readline().strip()
        return patterns, towels
    
def recurse(p, towels, i):
    if i >= len(p):
        return True
    for towel in towels:
        if p[i:i+len(towel)] == towel:
            if recurse(p, towels, i+len(towel)):
                return True
    return False

def add_up(p, towels, i, cache):
    if i in cache:
        return cache[i]
    if i >= len(p):
        return 1
    result = 0
    for towel in towels:
        if p[i:i+len(towel)] == towel:
            result += add_up(p, towels, i+len(towel), cache)
    cache[i] = result
    return result

patterns, towels = read_input()
result = 0
for p in patterns:
    if recurse(p, towels, 0):
        result += 1

print(f"p1: {result}")

result = 0
for p in patterns:
    cache = {}
    result += add_up(p, towels, 0, cache)

print(f"p2: {result}")