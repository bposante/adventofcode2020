# finds how many trees (marked by #) are in your path moving down 3 and right 1

day3input = open("aoc3input.txt", "r")
lines = lambda row: list(row)
trees = [lines(line.strip('\n')) for line in day3input]
length = len(trees)

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
