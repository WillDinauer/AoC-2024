def construct_map_and_list():
    with open("inputs/day5.txt", "r") as f:
        rules = {}
        rule = f.readline()
        while rule != "\n":
            nums = [int(i) for i in rule.strip().split("|")]
            if nums[0] not in rules:
                rules[nums[0]] = []
            rules[nums[0]].append(nums[1])
            rule = f.readline()
        
        updates = []
        u = f.readline()
        while u != "":
            updates.append([int(i) for i in u.strip().split(",")])
            u = f.readline()
        return rules, updates

def check_rules(rules, seen, cur):
    for x in seen:
        if x in rules[cur]:
            return False
    return True

def check_update(rules, update):
    seen = [update[0]]
    for i in range(1, len(update)):
        cur = update[i]
        if not check_rules(rules, seen, cur):
            return 0
        seen.append(cur)
    return seen[len(seen)//2]
    

def part1():
    rules, updates = construct_map_and_list()
    
    result = 0
    for update in updates:
        result += check_update(rules, update)

    return result

def fix_update(rules, update):
    return 0

def part2():
    rules, updates = construct_map_and_list()
    result = 0
    for update in updates:
        if check_update(rules, update) == 0:
            result += fix_update(rules, update)
    return result


if __name__ == "__main__":
    print(part1())