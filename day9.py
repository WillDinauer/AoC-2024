def read_line():
    with open("inputs/day9.txt", "r") as f:
        line = f.readline().strip()
        return [int(line[i]) for i in range(len(line))]
    
def sequence_sum(id, length, pos, offset):
    # Sum of arithmetic sequence
    return (id*length*(2*pos+2*offset+length-1))//2

def part1():
    line = read_line()
    result = 0
    pos = 0
    l = 0
    r = len(line)-1
    unfinished = False
    while l < r:
        unfinished = False
        result += sequence_sum(l//2, line[l], pos, 0)
        pos += line[l]
        i = 0
        while i < line[l+1]:
            capacity = line[l+1]-i
            if line[r] <= capacity:
                unfinished = False
                result += sequence_sum(r//2, line[r], pos, i)
                i += line[r]
                r -= 2
                if l >= r:
                    return result
            else:
                unfinished = True
                result += sequence_sum(r//2, capacity, pos, i)
                line[r] -= capacity
                break
        pos += line[l+1]
        l += 2
    if unfinished:
        result += sequence_sum(l//2, line[l], pos, 0)
    return result

def slot(line, i, pos):
    for l in range(1, i, 2):
        if line[l] >= line[i]:
            res = sequence_sum(i//2, line[i], pos[l], 0)
            line[l] -= line[i]
            pos[l] += line[i]
            return res
    return 0

def part2():
    line = read_line()
    result = 0
    cur = 0
    pos = {}
    for i, num in enumerate(line):
        pos[i] = cur
        cur += num

    for i in range(len(line)-1, -1, -2):
        res = slot(line, i, pos)
        if res == 0:
            res = sequence_sum(i//2, line[i], pos[i], 0)
        result += res
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())