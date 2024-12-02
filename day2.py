import copy

def extract_lines():
    lines = []
    with open("inputs/day2.txt", "r") as f:
        line = [int(i) for i in f.readline().split()]
        while (len(line) > 0):
            lines.append(line)
            line = [int(i) for i in f.readline().split()]
    return lines

def check_safe(line):
    if line[0] == line[1]:
        return False
    increasing = True if line[1] > line[0] else False
    for i in range(1, len(line)):
        if increasing:
            if line[i]-line[i-1] > 3 or line[i]-line[i-1] <= 0:
                return False
        else:
            if line[i-1]-line[i] > 3 or line[i-1]-line[i] <= 0:
                return False
    return True

def part1():
    lines = extract_lines()
    num_safe = 0
    for line in lines:
        if check_safe(line):
            num_safe += 1
    
    return num_safe

def part2():
    lines = extract_lines()
    num_safe = 0
    for line in lines:
        if check_safe(line):
            num_safe += 1
        else:
            for i in range(len(line)):
                line_cp = copy.deepcopy(line)
                line_cp.pop(i)
                if check_safe(line_cp):
                    num_safe += 1
                    break
    return num_safe
    
if __name__ == "__main__":
    print(part1())
    print(part2())