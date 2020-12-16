# a function that checks to see if the passwords are valid
# list[x][0][0]: lower limit, list[x][0][1]: upper limit, list[x][1]: letter, list[x][2]: password

def validpassword(list):
    # initialize counter for num of passwords
    countP = 0
    for nlist in list:
        for element in nlist:
            # assigns the required numbers to min and max
            if element == nlist[0]:
                minnum = element[0]
                maxnum = element[1]
                countL = 0
            # counts the time the required character appears in the password
            if element == nlist[2]:
                for character in element:
                    if character in nlist[1]:
                        countL += 1
                # checks if the password is valid
                if minnum <= countL and countL <= maxnum:
                    countP += 1
    return countP

# puts the information in a nested list
list1 = open("aoc2input.txt", "r")
passwords = [line.split() for line in list1]

for element in passwords:
    nums = element[0].split("-")
    element[0] = nums
    for x in element[0]:
        element[0][0] = int(element[0][0])
        element[0][1] = int(element[0][1])

def validpasswordspt2(list):
    for nlist in list:
        for element in nlist:
            # assigns the required numbers to min and max
            if element == nlist[0]:
                minnum = element[0]
                maxnum = element[1]
                countL = 0
            # counts the time the required character appears in the password
            if element == nlist[2]:
                for character in element:
                    if character in nlist[1]:
                        if character == element[minnum] ^ element[maxnum]:
                            countL += 1
            return countL

print(validpassword(passwords))
print(validpasswordspt2(passwords))