# a function that checks to see if the passwords are valid
# list[x][0][0]: lower limit, list[x][0][1]: upper limit, list[x][1]: letter, list[x][2]: password

# puts the information in a nested list
list1 = open("aoc2input.txt", "r")
passwords = [line.split() for line in list1]
list1.close

for element in passwords:
    nums = element[0].split("-")
    element[0] = nums
    for x in element[0]:
        element[0][0] = int(element[0][0])
        element[0][1] = int(element[0][1])


def validpassword(list):
    # initialize counter for num of passwords
    countP = 0
    for element in list:
        minnum = element[0][0]
        maxnum = element[0][1]
        letter = element[1].strip(": ")
        password = element[2]
        if minnum <= password.count(letter) <= maxnum:
            countP += 1
    return countP

print(validpassword(passwords))

def validpasswordspt2(list):
    countP = 0
    for element in list:
        minnum = element[0][0] -1
        maxnum = element[0][1] -1
        letter = element[1].strip(": ")
        password = element[2]
        if (password[minnum] == letter) != (password[maxnum] == letter):
            countP += 1
    return countP

print(validpasswordspt2(passwords))
