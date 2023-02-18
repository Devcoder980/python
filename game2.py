# Todo: Rock Paper Scisors Game
import random
import time
rock =1
paper=2
scissors=3
names={rock:"rock",paper:"Paper",scissors:"scissors"}
rules={rock:scissors,paper:rock,scissors:paper}
player_score=0
computer_score=0

def start():
    print("Lets play a game of rock , paper ,scissors.")
    while game():
        pass
    scores()
def game():
    player=move()
    computer=random.randint(1,3)
    result(player,computer)
    return play_again()

def move():
    while True:
        player=input("Rock=1\npaper=2\nscissors =3 \nMake a move:")
        try :
            player=int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oops! i didn't undestant hat .please enter 1,2,3")

def result(player,computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print("computer thre {0}".format(names[computer]))
    global player_score,computer_score
    if player==computer:
        print("Tie game.")
    else:
        if rules[player]==computer:
            print("your vitory has been assured.")
            player_score+=1
        else:
            print("The comput laughs as your realse you have been defated")
            computer_score +=1

def scores():
    global player_score ,computer_score
    print("high scores")
    print("player:",player_score)
    print("computer:",computer_score)

def play_again():
    answer=input("Would you like to play Agian y/n")
    if answer in("Y","y","yes","Yes","of course!"):
        return answer
    else:
        print("Thank you very much for playing our game. see you next time!")

if __name__=='__main__':
    start()
