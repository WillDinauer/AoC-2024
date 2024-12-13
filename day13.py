def get_nums(arr, f, d, p2=False):
    vals = f.readline().strip().split(",")
    addition = "10000000000000" if p2 else ""
    arr.append([int(addition+vals[0].split(d)[-1]), int(addition+vals[-1].split(d)[-1])])

def read_helper(f, a, b, p, p2=False):
    get_nums(a, f, "+")
    get_nums(b, f, "+")
    get_nums(p, f, "=", p2)

def read_input(p2=False):
    a = []
    b = []
    p = []
    with open("inputs/day13_ex.txt", "r") as f:
        read_helper(f, a, b, p, p2)
        while f.readline() != "":
            read_helper(f, a, b, p, p2)
    return a, b, p

def play(da, db, prize):
    cost = 500
    for a in range(101):
        for b in range(101):
            if da[0]*a + db[0]*b == prize[0] and da[1]*a + db[1]*b == prize[1]:
                cost = min(cost, a*3 + b)
    return 0 if cost == 500 else cost

def part1():
    a, b, prize = read_input()
    result = 0
    for i in range(len(a)):
        result += play(a[i], b[i], prize[i])
    return result

def part2():
    a, b, prize = read_input(True)
    return 0

if __name__ == "__main__":
    print(part1())
    print(part2())