#!/usr/bin/env/python3

question1 = "     Does it Move? Y or N  "
question2 = "     Should it Move? Y or N  "
movesolution = "     Spray some WD-40 on it. I put  that.. stuff on everthing"
nomovesolution = "    Wrap it up in duct tape!"       
nosolution = "     No Problem"
move = input(question1).capitalize()
shouldit = input(question2).capitalize()

def moves():
#    shouldit = input(question2).capitalize()
    if shouldit == "Y":
        print(nosolution)
    else:
        print(nomovesolution)

def doesnotmove():
#    shouldit = input(question2).capitalize()
    if shouldit == "Y": 
        print(nosolution)
    else:
        print(movesolution)

def main():
        if move == "Y":
            moves()
        else: doesnotmove()

main()
