import random

rows = 0


def init():
    colu = [None] * rows

    for i in range(rows):
        colu[i] = ['-'] * rows
    return colu


def display(colu):
    for i in range(0, rows):
        colu = list(colu)
        for j in range(0, rows):
            print(colu[i][j], end=" ")
        print('\n')
    return


def playermove(colu):
    rowp = int(input("enter row no"))
    colp = int(input("enter column no"))
    rowp = rowp - 1
    colp = colp - 1

    if (colu[rowp][colp] == '-'):
        colu[rowp][colp] = 'X'
    elif (colu[rowp][colp] == 'O' or colu[rowp][colp] == 'X'):
        print("please enter another move")
        playermove(colu)
    else:
        print("incorrect move")
        playermove(colu)
    return


def computermove(colu):
    colc = random.randint(0, rows-1)
    rowc = random.randint(0, rows-1)
    if (colu[rowc][colc] == '-'):
        colu[rowc][colc] = 'O'
    elif (colu[rowc][colc] == 'X' or colu[rowc][colc] == 'O'):
        computermove(colu)
    else:
        print("incorrect move")
    return


def checkplayervictory(colu):
    d1count = 0
    d2count = 0

    for i in range(rows):
        hcount = 0
        for j in range(rows):
            if (colu[i][j] == 'X'):
                hcount += 1
            if (hcount == rows):
                return True
    for i in range(rows):
        vcount = 0
        for j in range(rows):
            if (colu[j][i] == 'X'):
                vcount += 1
            if (vcount == rows):
                return True

    i = 0
    j = 0
    while (i < rows - 1 and j < rows - 1):

        if (colu[i][j] == 'X' and (colu[i][j] == colu[i + 1][j + 1])):
            d1count += 1
        if (d1count == rows - 1):
            return True

        i += 1
        j += 1

    i = 0
    j = rows - 1

    while (i < rows - 1 and j > 0):

        if (colu[i][j] == 'X' and (colu[i][j] == colu[i + 1][j - 1])):
            d2count += 1
        if (d2count == rows - 1):
            return True

        i += 1
        j -= 1

    return False


def checkcomputervictory(colu):
    d1count = 0
    d2count = 0

    for i in range(rows):
        hcount = 0
        for j in range(rows):
            if (colu[i][j] == 'O'):
                hcount += 1
            if (hcount == rows):
                return True
    for i in range(rows):
        vcount = 0
        for j in range(rows):
            if (colu[j][i] == 'O'):
                vcount += 1
            if (vcount == rows):
                return True

    i = 0
    j = 0
    while (i < rows - 1 and j < rows - 1):

        if (colu[i][j] == 'O' and (colu[i][j] == colu[i + 1][j + 1])):
            d1count += 1
        if (d1count == rows - 1):
            return True

        i += 1
        j += 1

    i = 0
    j = rows - 1

    while (i < rows - 1 and j > 0):

        if (colu[i][j] == 'O' and (colu[i][j] == colu[i + 1][j - 1])):
            d2count += 1
        if (d2count == rows - 1):
            return True

        i += 1
        j -= 1

    return False


def drawcheck(colu):
    for i in range(rows):
        for j in range(rows):
            if (colu[i][j] == '-'):
                return False


    return True

if __name__ == '__main__':
    rows = int(input("enter rows"))
    colu = init()
    display(colu)
    while (checkplayervictory(colu) == False):

        playermove(colu)

        if (checkplayervictory(colu) == True):
            print("player wins")
            break
        computermove(colu)
        display(colu)

        if (checkcomputervictory(colu) == True):
             print("computer wins")
             break

        if(drawcheck(colu)):
            print("draw")
            break

