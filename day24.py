import copy

def read_inputs():
    with open("inputs/day24.txt", "r") as f:
        arr = []
        line = f.readline().strip()
        while line != "":
            line = line.split(": ")
            arr.append([line[0], int(line[1])])
            line = f.readline().strip()

        ins = []
        line = f.readline().strip()
        while line != "":
            ins.append(line.split())
            line = f.readline().strip()
    return arr, ins

def resolve_value(m, c="z"):
    keys = list(m.keys())
    keys.sort(reverse=True)
    p1 = 0
    for key in keys:
        if key[0] == c:
            p1 = p1 << 1
            p1 |= m[key]
    return p1

def handle_swap(og, a, b):
    for i in range(len(og)):
        if og[i][-1] == a:
            c = i
        elif og[i][-1] == b:
            d = i
    og[c][-1], og[d][-1] = og[d][-1], og[c][-1]

def calculate(m, g):
    while len(g) > 0:
        ni = []
        for i in g:
            if i[0] not in m or i[2] not in m:
                ni.append(i)
                continue
            if i[1] == "AND":
                res = m[i[0]] & m[i[2]]
            elif i[1] == "XOR":
                res = m[i[0]] ^ m[i[2]]
            elif i[1] == "OR":
                res = m[i[0]] | m[i[2]] 
            m[i[-1]] = res
        if ni == g:
            return 0
        g = ni
    return resolve_value(m)

arr, og = read_inputs()
m = {}
for entry in arr:
    m[entry[0]] = entry[1]
g = copy.deepcopy(og)
p1 = calculate(m, g)
print(f"p1: {p1}")

# These were found one-by-one via exception handling
swaps = [["vss", "z14"], ["kdh", "hjf"], ["z31", "kpp"], ["z35", "sgj"]]
for swap in swaps:
    handle_swap(og, swap[0], swap[1])

m = {}
for entry in og:
    m[entry[0], entry[1], entry[2]] = entry[-1]
    m[entry[2], entry[1], entry[0]] = entry[-1]

arr.sort()
n = len(arr)//2
carry = m[arr[0][0], "AND", arr[n][0]]
for i in range(1, n):
    x = arr[i][0]
    y = arr[n + i][0]
    try:
        a = m[x, "XOR", y]
        b = m[x, "AND", y]
        z = m[a, "XOR", carry]
        if z[0] != "z":
            raise Exception(f"Expected 'z{x[1:]}, got '{z}'")
        d = m[a, "AND", carry]
        carry = m[b, "OR", d]
    except Exception as err:
        print(err)
        print(f"Failed on full addr {i}")
        break

wires = []
for swap in swaps:
    wires.append(swap[0])
    wires.append(swap[1])
wires.sort()
result = wires[0]
for i in range(1, len(wires)):
    result+=","+wires[i]
print(f"p2: {result}")