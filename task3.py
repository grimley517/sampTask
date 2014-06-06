'''
create a program  that takes in a 10 digit number, and outputs the isbn check digit

'''
def getChkDig(inStr):
    sumRes = 0
    for i in range (len(inStr)):
        num = inStr[i]
        num = int(num)
        num = num*(11-i)
        sumRes += num
    remainder = sumRes % 11
    if remainder == 0:
        return (0)
    answer = 11 - remainder
    if answer == 10:
        answer = 'X'

    return (answer)