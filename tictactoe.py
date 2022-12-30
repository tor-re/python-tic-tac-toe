import sys, time 
asciiArt = ['  _______ _____ _____   _______       _____   _______ ____  ______ \n',' |__   __|_   _/ ____| |__   __|/\   / ____| |__   __/ __ \|  ____|\n','    | |    | || |         | |  /  \ | |         | | | |  | | |__   \n','    | |    | || |         | | / /\ \| |         | | | |  | |  __|  \n','    | |   _| || |____     | |/ ____ \ |____     | | | |__| | |____ \n','    |_|  |_____\_____|    |_/_/    \_\_____|    |_|  \____/|______|\n']
c = input("wanna play [y/n] \n")
if c == "y":
    turn = "x"
    gameRunning = True
    for a in range(len(asciiArt)):
        for b in asciiArt[a]:
            sys.stdout.write(b)
            sys.stdout.flush()
            time.sleep(0.01)
else:
    gameRunning = False
    print("why are you here?")

valuesForChecks = [1, 2, 3]
top = [" "," "," "]
cen = [" "," "," "]
bot = [" "," "," "]

def printRow(row):
    sys.stdout.write("|")
    for i in range(len(row)):
        sys.stdout.write(str(row[i]))
        if i < 2:
            sys.stdout.write("    ")
        sys.stdout.flush()
    sys.stdout.write("|")
    #second wall
    print("\n")
while gameRunning:
    print("_____________")
    printRow(top)
    printRow(cen)
    printRow(bot)
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
    spot = int(input("pick a spot 1 being top left 9 being bottom right: "))
    if spot - 1 <= 2 and top[spot - 1] == " ":
        top[spot - 1] = turn
        change = True
    elif spot >= 4 and spot <= 6 and cen[spot - 4] == " ":
            cen[spot - 4] = turn
            print(cen[spot - 4])
            change = True
    elif spot >= 7 and bot[spot - 7] == " ":
            bot[spot - 7] = turn
            change == True
    for _ in range(len(top)):
        if top[_] == cen[_] == bot[_] == turn:
            gameRunning = False
            print("win " + turn)
            print("_____________")
            printRow(top)
            printRow(cen)
            printRow(bot)
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if top[0] == top[1] == top[2] == turn:
        gameRunning = False
        print("win " + turn)
        print("_____________")
        #top boarder
        printRow(top)
        printRow(cen)
        printRow(bot)
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if cen[0] == cen[1] == cen[2] == turn:
        gameRunning = False
        print("win " + turn)
        print("_____________")
        printRow(top)
        printRow(cen)
        printRow(bot)
        #all rows
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if bot[0] == bot[1] == bot[2] == turn:
        gameRunning = False
        print("win " + turn)
        print("_____________")
        printRow(top)
        printRow(cen)
        printRow(bot)
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if turn == "x":
        turn = "o"
    elif turn == "o":
        turn = "x"
