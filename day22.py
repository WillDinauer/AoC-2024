nums = [int(i) for i in open("inputs/day22.txt", "r").read().split("\n")]

mn = 16777216
def apply(n):
    n = (n ^ (n << 6)) % mn
    n = (n ^ (n >> 5)) % mn
    n = (n ^ (n << 11)) % mn
    return n

p1 = 0
for n in nums:
    for _ in range(2000):
        n = apply(n)
    p1 += n
print(f"p1: {p1}")