def read_line():
    with open("inputs/day11.txt", "r") as f:
        return f.readline().strip().split()
    

def consider_stone(stone, blinks):
    stones = [stone]
    for _ in range(25):
        ns = []
        for i in range(len(stones)):
            if stones[i] == "0":
                ns.append("1")
            elif len(stones[i]) % 2 == 0:
                mid = len(stones[i])//2
                ns.append(str(int(stones[i][:mid])))
                ns.append(str(int(stones[i][mid:])))
            else:
                ns.append(str(int(stones[i]) * 2024))
        stones = ns
    return len(stones)


def part1():
    stones = read_line()
    result = 0
    for stone in stones:
        result += consider_stone(stone, 25)
    return result

def part2():
    pass

if __name__ == "__main__":
    print(part1())
    print(part2())