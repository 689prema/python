#import random
from random import randint
player_wins = 0
computer_wins = 0
winning_score = 2
while player_wins < winning_score and computer_wins < winning_score:
    print("Player score:{} Computer score: {}".format(player_wins,computer_wins))
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    
    player = input("Player,make your move:").lower()
    if player == "quit" or player == "q":
        break
    #rand_num = random.randint(0,2)
    rand_num = randint(0,2)
    if rand_num ==0:
        computer="rock"
    elif rand_num ==1:
         computer = "paper"
    else:
        computer ="scissors"
    print("Computer plays {}".format(computer))
    
    if player == computer:
        print("It's a tie!")
    elif player =="rock":
        if computer =="scissors":
            print("player wins")
            player_wins +=1
        elif computer =="paper":
            print("computer wins!")
            computer_wins +=1
    elif player =="paper":
        if computer =="rock":
            print("player wins!")
            player_wins +=1
        elif computer=="scissors":
            print("computer wins!")
            computer_wins +=1
    elif player =="scissors":
        if computer =="rock":
          print("computer wins!")
          computer_wins +=1
        elif computer =="paper":
          print("player wins!")
          player_wins +=1
    else:
      print("Please enter valid move")
if player_wins > computer_wins:
    print("CONGRATS, YOU WON..!")
elif player_wins == computer_wins:
    print("TIE")
else:
    print("OH NO :(THE COMPUTER WON..")
#print("FINAL SCORES...Player score:{} Computer score: {}".format(player_wins,computer_wins))