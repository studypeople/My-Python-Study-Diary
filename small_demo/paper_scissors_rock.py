import random

def computer():
    ran = random.randint(1, 3)
    computer_sc = ""
    if ran == 1:
        computer_sc = "stone"
    elif ran == 2:
        computer_sc = "cut"
    elif ran == 3:
        computer_sc = "paper"
    print("电脑出了：",computer_sc)
    return computer_sc


def win_or_fail(people_sc, computer_sc):
    result = ""
    if people_sc == "stone" and computer_sc == "stone":
        result = "ping"
    elif people_sc == "stone" and computer_sc == "cut":
        result = "win" 
    elif people_sc == "stone" and computer_sc == "paper":
        result = "fail"
    elif people_sc == "cut" and computer_sc == "stone":
        result = "fail"
    elif people_sc == "cut" and computer_sc == "cut":
        result = "ping"
    elif people_sc == "cut" and computer_sc == "paper":
        result = "win"
    elif people_sc == "paper" and computer_sc == "stone":
        result = "win"
    elif people_sc == "paper" and computer_sc == "cut":
        result = "fail"
    elif people_sc == "paper" and computer_sc == "papaer":
        result = "ping"
    return result

people_sc = input()
computer_sc = computer()
print(win_or_fail(people_sc, computer_sc)) 