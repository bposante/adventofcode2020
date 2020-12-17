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
def diffslopes(list1):
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    multiplied = 1
    for slope in slopes:
        treecount = 0 
        x = 0
        y = 0
        while y < len(list1):
            if list1[y][x] == "#":
                treecount += 1
                y += slope[1]
                x = (x + slope[0]) % 31
            else:    
                y += slope[1]
                x = (x + slope[0]) % 31
        slope.append(treecount)
        multiplied *= slope[2]
    return multiplied

print(diffslopes(trees))
