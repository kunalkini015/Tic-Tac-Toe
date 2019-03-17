"""*********** TIC TAC TOE ************"""
def draw(a):
    print(a[0], end="")
    print(" |", a[1], end="")
    print(" |", a[2], end="\n")
    print("__ ___  __", end="\n")
    print(a[3], end="")
    print(" |", a[4], end="")
    print(" |", a[5], end="\n")
    print("__ ___  __", end="\n")
    print(a[6], end="")
    print(" |", a[7], end="")
    print(" |", a[8], end="\n")

def win(a):
    if a[0] == a[1] == a[2]or a[4] == a[5] == a[3]or a[6] == a[7] == a[8]:
        return True
    elif a[0] == a[3] == a[6]or a[1] == a[4] == a[7]or a[2] == a[5] == a[8]:
        return True
    elif a[0] == a[4] == a[8]or a[2] == a[4] == a[8]:
        return True
    else:
        return False

def player_1(a, p1):
    choice = int(input("{}, Enter the choice".format(p1)))
    a[choice-1] = 'X'
    draw(a)
    if win(a) == True:
        print("wooooohooo, Congratz {} \n YOU ARE THE WINNER".format(p1))
        if a[0] == '1':
            a[0] = ' '
        if a[1] == '2':
            a[1] = ' '
        if a[2] == '3':
            a[2] = ' '
        if a[3] == '4':
            a[3] = ' '
        if a[4] == '5':
            a[4] = ' '
        if a[5] == '6':
            a[5] = ' '
        if a[6] == '7':
            a[6] = ' '
        if a[7] == '8':
            a[7] = ' '
        if a[8] == '9':
            a[8] = ' '
        draw(a)
        return True
    else:
        return
def player_2(a, p2):
    choice = int(input("{}, Enter the choice".format(p2)))
    a[choice-1] = 'O'
    draw(a)
    if win(a) == True:
        print("wooooohooo, Congratz {} \n YOU ARE THE WINNER".format(p2))
        if a[0] == '1':
            a[0] = ' '
        if a[1] == '2':
            a[1] = ' '
        if a[2] == '3':
            a[2] = ' '
        if a[3] == '4':
            a[3] = ' '
        if a[4] == '5':
            a[4] = ' '
        if a[5] == '6':
            a[6] = ' '
        if a[6] == '7':
            a[6] = ' '
        if a[7] == '8':
            a[7] = ' '
        if a[8] == '9':
            a[8] = ' '
        draw(a)
        return True
    else:
        return

def tic():
    print("\n")
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("Welcome To the Tic tak toe")
    draw(a)
    p1 = input("enter player 1's name\n")
    p2 = input("enter player 2's name\n")
    count = 0
    while count <= 8:
        if player_1(a, p1) == True:
            break
        elif player_2(a, p2) == True:
            break
        count += 2
tic()

