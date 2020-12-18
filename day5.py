# bailey posante
# 12/17/2020
# advent of code day 5 puzzle

with open("aoc5input.txt") as file:
    boardingpasses = file.read().split()
    #print(boardingpasses)

def puzzle1(list1):
    seatid = 0
    seatidlist = []
    for i in list1:
        x = 0
        y = 127
        x2 = 0
        y2 = 7
        for character in i:
            diff = y - x
            diff2 = y2 - x2
            if character == "F":
                y = x + diff // 2
            if character == "B":
                x = x + diff // 2
            if character == "L":
                y2 = x2 + diff2 // 2
            if character == "R":
                x2 = x2 + diff2 // 2 
        seat = y * 8 + y2
        seatidlist.append(seat)
        if y * 8 + y2 > seatid:
            seatid = y * 8 + y2
    # part 2
    seatidlist.sort()
    print([seat for seat in range(seatidlist[0], seatidlist[-1] + 1) if seat not in seatidlist])
    return seatid


test = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
print(puzzle1(boardingpasses))