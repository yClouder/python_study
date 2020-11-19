import random

rock = random.randint(0,1)
home01 = 0
home02 = 0

def chosewHand():
    user_inp = input("Chose in what hand are the rock.(Right or Left)")
    rock = random.randint(0,1)
    global home01
    if user_inp.lower() == "right":
        if rock == 1:
            print("Youre right, move one step.")
            home01 = home01 + 1
        else:
            print("Youre wrong, stay.")
    elif user_inp.lower() == "left":
        if rock == 0:
            print("Youre right, move one step.")
            home01 = home01 + 1
        else:
            print("Youre wrong, stay.")
    else:
        print("Pleasse digit somethin that i can understand.")
        return chosewHand()



def selectHand():
    user_inp = input("In what hand youre puting the rock?(Right or Left)")
    rock = random.randint(0,1)
    global home02
    if user_inp == "right":
        if rock == 1:
            print("The bot is right, move one step.")
            home02 = home02 + 1
        else:
            print("The bot is wrong, stay.")
    elif user_inp.lower() == "left":
        if rock == 0:
            print("The bot is right, move one step.")
            home02 = home02 + 1
        else:
            print("The bot is wrong, stay.")
    else:
        print("Pleasse digit somethin that i can understand.")
        return selectHand()

while home01 < 5 or home02 < 5:
    print(home01)
    print(home02)
    chosewHand()
    selectHand()

if home01 == 5:
    print("You won the game.")
else:
    print("The bot won the game.")
