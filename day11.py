def read_line():
    with open("inputs/day11.txt", "r") as f:
        return f.readline().strip().split()

def consult_oracle(stone, oracle, blinks, offset):
    result = 0
    stones = [stone]
    for b in range(blinks, -1 + offset, -1):
        ns = []
        for s in stones:
            if len(s) == 1 and int(s)%2 == 0:
                i = 0
                match s:
                    case "2":
                        i = 1
                    case "4":
                        i = 2
                    case "6":
                        i = 3
                    case "8":
                        i = 4
                result += oracle[b - offset][i]
            elif len(s)%2 == 0:
                mid = len(s)//2
                ns.append(str(int(s[:mid])))
                ns.append(str(int(s[mid:])))
            else:
                ns.append(str(int(s) * 2024))
        stones = ns
    return result + len(stones)

def construct_oracle(oracle, blinks):
    stones = ["1", str(2024*2), str(2024*4), str(2024*6), str(2024*8)]
    for b in range(blinks):
        for idx, stone in enumerate(stones):
            oracle[b][idx] = consult_oracle(stone, oracle, b, 1)


def handle_stones(blinks):
    stones = read_line()
    oracle = [[0 for _ in range(5)] for _ in range(blinks)]
    construct_oracle(oracle, blinks)
    
    result = 0
    for stone in stones:
        result += consult_oracle(stone, oracle, blinks-1, 0)
    return result

def part1():
    return handle_stones(25)

def part2():
    return handle_stones(75)
    

if __name__ == "__main__":
    print(part1())
    print(part2())