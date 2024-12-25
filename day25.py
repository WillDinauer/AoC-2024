kal = open("inputs/day25.txt", "r").read().split("\n\n")
for i in range(len(kal)):
    kal[i] = kal[i].split("\n")

def measure_col(a, el, c):
    for r in range(len(a)):
        if a[r][c] != el:
            return r-1
    return -1

def measure(a, el):
    result = []
    for c in range(len(a[0])):
        result.append(measure_col(a, el, c))
    return result

def fit(key, lock, goal):
    for i in range(len(key)):
        if key[i] + lock[i] > goal:
            return 0
    return 1

locks = []
keys = []
for el in kal:
    if el[0][0] == "#":
        locks.append(measure(el, "#"))
    else:
        keys.append([len(el)-2-i for i in measure(el, ".")])

length = len(kal[0])-2
p1 = 0
for lock in locks:
    for key in keys:
        p1 += fit(key, lock, length)
print(f"p1: {p1}")