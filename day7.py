def read_lines():
    with open("inputs/day7.txt", "r") as f:
        line = f.readline()
        targets = []
        nums = []
        while (line != ""):
            line = line.strip().split()
            targets.append(int(line[0][:len(line[0])-1]))
            line = [int(line[i]) for i in range(1, len(line))]
            nums.append(line)
            line = f.readline()
        return targets, nums
    
def recurse(target, line, idx, cur):
    if idx == len(line):
        return cur == target
    return recurse(target, line, idx+1, cur+line[idx]) or recurse(target, line, idx+1, cur*line[idx])

def evaluate_line(target, line):
    return target if recurse(target, line, 1, line[0]) else 0

    
def part1():
    targets, nums = read_lines()
    result = 0
    for i, line in enumerate(nums):
        result += evaluate_line(targets[i], line)
    return result

def special_recurse(target, line, idx, cur):
    if idx == len(line):
        return cur == target
    return special_recurse(target, line, idx+1, cur+line[idx]) or special_recurse(target, line, idx+1, cur*line[idx]) or special_recurse(target, line, idx+1, int(str(cur) + str(line[idx])))

def special_eval(target, line):
    return target if special_recurse(target, line, 1, line[0]) else 0
        
def part2():
    targets, nums = read_lines()
    result = 0
    for i, line in enumerate(nums):
        result += special_eval(targets[i], line)
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())