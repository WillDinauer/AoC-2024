def read_input():
    with open("inputs/day21.txt", "r") as f:
        codes = [line.strip() for line in f.readlines()]
        return codes
    
def print_code(cur):
    for i in range(len(cur[0])):
        print(cur[0][i]*cur[1][i], end="")
    print()

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

def handle(result, pos, cur, num, m):
    r = cur[0] - pos[0]
    c = cur[1] - pos[1]

    # Prioritize "<" and "v" if possible
    if c < 0 and [pos[0], pos[1]+c] != m["x"]:
        result[0] += "<"
        result[1].append(-c)
        c = 0
    if r > 0 and [pos[0]+r, pos[1]] != m["x"]:
        result[0] += "v"
        result[1].append(r)
        r = 0

    # General directions
    if c > 0:
        result[0] += ">"
        result[1].append(c)
    if r > 0:
        result[0] += "v"
        result[1].append(r)
    elif r < 0:
        result[0] += "^"
        result[1].append(-r)
    if c < 0:
        result[0] += "<"
        result[1].append(-c)

    # Press it as many times as necessary
    result[0] += "A"
    result[1].append(num)


def process(cur, m):
    pos = m["A"]
    result = ["", []]
    for i in range(len(cur[0])):
        handle(result, pos, m[cur[0][i]], cur[1][i], m)
        pos = m[cur[0][i]]
    return result

codes = read_input()
result = 0
for code in codes:
    cur = [code, [1 for _ in range(len(code))]]
    cur = process(cur, keypad)
    for _ in range(2):
        cur = process(cur, remote)
    result += sum(cur[1]) * int(code[:3])
print(f"p1: {result}")