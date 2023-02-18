# Todo:Game for Random Number Generator

import random
import time

count = 0

def game():
    usernum = int(input("Enter the value your coice"))
    computnum = random.randint(1, 10)

    global count
    count += 1
    time.sleep(0.5)
    print(".....")
    time.sleep(0.5)
    print(".....")
    print("COmputer Chose Number is:", computnum)
    if usernum == computnum:
        print("you are wone")
        print("you in {0} times".format(count))
    else:
        chose = input("Your whatn to play again:y/n")
        if chose in ["y", "Y"]:
            game()
        else:
            print("Thank you for play")


game()
print("you Try {0} times".format(count))
