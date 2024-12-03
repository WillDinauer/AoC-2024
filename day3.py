def get_lines():
    with open("inputs/day3.txt", "r") as f:
        return f.readlines()

def part1():
    input = get_lines()
    res = 0
    for line in input:
        for i in range(len(line)-8):
            if line[i:i+4] != "mul(":
                continue
            n1 = 0
            j = i+4
            while line[j].isnumeric():
                n1 *= 10
                n1 += int(line[j])
                j += 1
            if line[j] != ",":
                continue
            j += 1
            n2 = 0
            while line[j].isnumeric():
                n2 *= 10
                n2 += int(line[j])
                j += 1
            if line[j] != ")" or n1 == 0 or n2 == 0:
                continue
            res += (n1 * n2)
    return res

def part2():
    input = get_lines()
    res = 0
    active = True
    for line in input:
        for i in range(len(line)-4):
            if line[i:i+4] == "do()":
                active = True
                i += 1
            elif i <= len(line)-7 and line[i:i+7] == "don't()":
                active = False
                i += 1
            elif active and line[i:i+4] == "mul(":
                n1 = 0
                j = i+4
                while line[j].isnumeric():
                    n1 *= 10
                    n1 += int(line[j])
                    j += 1
                if line[j] != ",":
                    continue
                j += 1
                n2 = 0
                while line[j].isnumeric():
                    n2 *= 10
                    n2 += int(line[j])
                    j += 1
                if line[j] != ")" or n1 == 0 or n2 == 0:
                    continue
                res += (n1 * n2)
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())