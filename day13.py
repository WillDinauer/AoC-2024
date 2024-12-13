def get_nums(arr, f, d, p2=False):
    vals = f.readline().strip().split(",")
    addition = 10000000000000 if p2 else 0
    arr.append([addition + int(vals[0].split(d)[-1]), addition + int(vals[-1].split(d)[-1])])

def read_helper(f, a, b, p, p2=False):
    get_nums(a, f, "+")
    get_nums(b, f, "+")
    get_nums(p, f, "=", p2)

def read_input(p2=False):
    a = []
    b = []
    p = []
    with open("inputs/day13.txt", "r") as f:
        read_helper(f, a, b, p, p2)
        while f.readline() != "":
            read_helper(f, a, b, p, p2)
    return a, b, p

def solve_diff(a, b, prize):
    denom = b[1]*a[0]-b[0]*a[1]
    num_a = (prize[0]*b[1]-prize[1]*b[0])/denom
    num_b = (prize[1]*a[0]-prize[0]*a[1])/denom
    return int(num_a), int(num_b)

def play(a, b, prize):
    num_a, num_b = solve_diff(a, b, prize)
    if num_a*a[0] + num_b*b[0] == prize[0] and num_a*a[1] + num_b*b[1] == prize[1]:
        return 3*num_a + num_b
    return 0
    
def handle_game(big=False):
    a, b, prize = read_input(big)
    result = 0
    for i in range(len(a)):
        result += play(a[i], b[i], prize[i])
    return result

def part1():
    return handle_game()

def part2():
    return handle_game(True)

if __name__ == "__main__":
    print(part1())
    print(part2())