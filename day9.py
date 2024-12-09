def read_line():
    with open("inputs/day9.txt", "r") as f:
        line = f.readline().strip()
        return [int(line[i]) for i in range(len(line))]
    
def sequence_sum(d, x, p, i):
    # Sum of arithmetic sequence
    return (d*x*(2*p+2*i+x-1))//2

def part1():
    line = read_line()
    result = 0
    pos = 0
    l = 0
    r = len(line)-1
    unfinished = False
    while l < r:
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

def part2():
    pass
    

if __name__ == "__main__":
    print(part1())
    print(part2())