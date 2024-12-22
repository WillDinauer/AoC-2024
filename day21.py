def read_input():
    with open("inputs/day21.txt", "r") as f:
        codes = [line.strip() for line in f.readlines()]
        return codes

keypad = {
    "7": [0, 0],
    "8": [0, 1],
    "9": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "1": [2, 0],
    "2": [2, 1],
    "3": [2, 2],
    "x": [3, 0],
    "0": [3, 1],
    "A": [3, 2],
}

remote = {
    "x": [0, 0],
    "^": [0, 1],
    "A": [0, 2],
    "<": [1, 0],
    "v": [1, 1],
    ">": [1, 2]
}

def get_sequences(a, b, r, c, m):
    # Horizontal 
    h = ""
    if c > 0:
        h = ">" * c
    elif c < 0:
        h = "<" * -c
    
    # Vertical
    v = ""
    if r > 0:
        v = "v" * r
    elif r < 0:
        v = "^" * -r

    # Potential sequences
    htov = h + v + "A"
    vtoh = v + h + "A"

    # Validate sequences
    sequences = []
    if [a+r, b] != m["x"]:
        sequences.append(vtoh)
    if [a, b+c] != m["x"]:
        sequences.append(htov)
    return sequences
    

def handle(a, b, r, c, d, cache, limit=2):
    if r == 0 and c == 0:
        return 1
    if (a, b, r, c, d) in cache:
        return cache[(a, b, r, c, d)]
    if d == limit:
        return abs(r) + abs(c) + 1
    m = keypad if d == 0 else remote
    sequences = get_sequences(a, b, r, c, m)
    result = float('inf')
    for seq in sequences:
        prev = "A"
        length = 0
        for i in range(len(seq)):
            na, nb = remote[prev]
            ny, nz = remote[seq[i]]
            nr = ny-na
            nc = nz-nb
            length += handle(na, nb, nr, nc, d+1, cache, limit)
            prev = seq[i]
        result = min(result, length)
    cache[(a, b, r, c, d)] = result
    return result

def process(code, cache, limit=2):
    prev = "A"
    length = 0
    for i in range(len(code)):
        a, b = keypad[prev]
        y, z = keypad[code[i]]
        r = y-a
        c = z-b
        length += handle(a, b, r, c, 0, cache, limit)
        prev = code[i]
    return length

codes = read_input()
p1, p2 = 0, 0
c1, c2 = {}, {}
for code in codes:
    l1 = process(code, c1, 2)
    l2 = process(code, c2, 25)
    p1 += l1 * int(code[:3])
    p2 += l2 * int(code[:3])
print(f"p1: {p1}")
print(f"p2: {p2}")