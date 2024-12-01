def create_lists():
    with open("inputs/day1.txt", "r") as file:
        l1 = []
        l2 = []
        x = file.readline()
        while x != "":
            ids = x.split()
            l1.append(int(ids[0]))
            l2.append(int(ids[1]))
            x = file.readline()
        return l1, l2

def part1():
    l1, l2 = create_lists()
        
    total = 0
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    print(f"Total distance: {total}")

def part2():
    l1, l2 = create_lists()
    
    total = 0
    for n1 in l1:
        freq = 0
        for n2 in l2:
            if n1 == n2:
                freq += 1
        total += freq * n1
    print(f"Similarity score: {total}")

if __name__ == "__main__":
    part1()
    part2()