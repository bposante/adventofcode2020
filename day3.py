# finds how many trees (marked by #) are in your path moving down 3 and right 1

day3input = open("aoc3input.txt", "r")
lines = lambda row: list(row)
trees = [lines(line.strip('\n')) for line in day3input]
length = len(trees)

# part 1
# right 3 down 1
def counttrees(list1):
    treecount = 0
    x = 0
    y = 0
    while y < len(list1):
        if list1[y][x] == "#":
            treecount += 1
            y += 1
            x = (x + 3) % 31
        else:    
            y += 1
            x = (x + 3) % 31
    return treecount
    
print(counttrees(trees))

# part 2
# right 1 down 1
def right1down1(list1):
    treecount = 0
    x = 0
    y = 0
    while y < len(list1):
        if list1[y][x] == "#":
            treecount += 1
            y += 1
            x = (x + 1) % 31
        else:    
            y += 1
            x = (x + 1) % 31
    return treecount

print(right1down1(trees))

# right 5 down 1
def right5down1(list1):
    treecount = 0
    x = 0
    y = 0
    while y < len(list1):
        if list1[y][x] == "#":
            treecount += 1
            y += 1
            x = (x + 5) % 31
        else:    
            y += 1
            x = (x + 5) % 31
    return treecount

print(right5down1(trees))

# right 7 down 1
def right7down1(list1):
    treecount = 0
    x = 0
    y = 0
    while y < len(list1):
        if list1[y][x] == "#":
            treecount += 1
            y += 1
            x = (x + 7) % 31
        else:    
            y += 1
            x = (x + 7) % 31
    return treecount

print(right7down1(trees))

# right 1 down 2
def right1down2(list1):
    treecount = 0
    x = 0
    y = 0
    while y < len(list1):
        if list1[y][x] == "#":
            treecount += 1
            y += 2
            x = (x + 1) % 31
        else:    
            y += 2
            x = (x + 1) % 31
    return treecount

print(right1down2(trees))
