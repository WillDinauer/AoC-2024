def read_input():
    with open("inputs/day19.txt", "r") as f:
        lines = f.read().strip().split("\n")
    towels = lines[0].split(", ")
    patterns = lines[2:]
    return towels, patterns

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

if __name__ == "__main__":
    towels, patterns = read_input()
    p1 = 0
    p2 = 0
    for p in patterns:
        cache = {}
        res = add_up(p, towels, 0, cache)
        if res > 0:
            p1 += 1
            p2 += res

    print(f"p1: {p1}\np2: {p2}")