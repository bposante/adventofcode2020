# a function that finds two numbers in a list that add to 2020, then multiplies them together

def find2num(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == 2020:
                return list[i] * list[j]
                 
def find3num(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            for k in range(j + 1, len(list)):
                if list[i] + list[j] + list[k] == 2020:
                    return list[i] * list[j] * list[k]

aocinput = open("aoc1input.txt", "r")

list1 = [int(line) for line in aocinput]

print(find2num(list1)) 
print(find3num(list1))
