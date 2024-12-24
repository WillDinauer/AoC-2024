def read_inputs():
    with open("inputs/day24.txt", "r") as f:
        m = {}
        line = f.readline().strip()
        while line != "":
            line = line.split(": ")
            m[line[0]] = int(line[1])
            line = f.readline().strip()

        ins = []
        line = f.readline().strip()
        while line != "":
            ins.append(line.split())
            line = f.readline().strip()
    return m, ins

m, ins = read_inputs()
while len(ins) > 0:
    ni = []
    for i in ins:
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
    ins = ni
keys = list(m.keys())
keys.sort(reverse=True)
p1 = 0
for key in keys:
    if key[0] == "z":
        p1 = p1 << 1
        p1 |= m[key]
print(f"p1: {p1}")