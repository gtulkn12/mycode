#!/usr/bin/env python3
message = ('    Time to make America Great Again ')
months = (["jan", "feb", "mar", "apr" "may", "jun"], ["jul", "aug", "sep", "oct", "nov", "dec"])
weekdays = (["mon", "tue", "wed"], ["thu", "fri", "sat", "sun"])

def main():
    print(message)
    birthMonth =input("     What are the first three letters of your Birth Month?  ").lower()
    birthDayOfTheWeek = input("     What are the first 3 letters of the Weekday you were born?  ").lower()
    marine() if birthMonth in months[0] and weekdays[0] else army() if  birthMonth in months[1] and weekdays[0] else navy() if birthMonth in months[0] and weekdays[2] else airforce()

def marine():
    jarhead = input("     Do you like Jars? Y or N  " ).capitalize()
    if jarhead == "Y":
        print("     Great, you would make a great  Marine")
    else:
        print("     To Bad, you are destined to be a Jar Head Marine")

def army():
    soldier  = input("     Do you like being Great? Y or N  " ).capitalize()
    if soldier == "Y":
        print("     Great, you would make a great Soldier")
    else:
        marine()

def navy():
    squid = input("     Do you like Bell Bottoms? Y or N  " ).capitalize()
    if squid == "Y":
        print("     Great, you would make a great Navy Squid")
    else:
        marine()

def airforce():
    cheerleader = input("     Do you like being a Cheer Leader? Y or N  " ).capitalize()
    if cheerleader == "Y":
        print("     Great you will make a great Cheer Force Range")
    else:
        marine()

def playagain():
    playagain = input("    Would you like to play again?"  ).capitalize()
    if playagain == "Y":
        main()
    else:
        print("Thanks for playing")

main()

# Comment
#if birthMonth in months[0] and weekdays[0]:
#    marine()
#elif birthMonth in months[1] and weekdays[0]:
#    army()
#elif birthMonth in months[0] and weekdays[2]:
#    navy()
#elif birthMonth in months[2] and weekdays[2]:
#    airforce()
#
#else: print("none")

