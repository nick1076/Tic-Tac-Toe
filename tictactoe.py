import random as r
import os

player_move = 0
ai_move = 0

def game():
    choice = input("What is your choice? (r/p/s) | My choice: ")
    if (choice == "r"):
        player_move = 0
    elif (choice == "p"):
        player_move = 1
    elif (choice == "s"):
        player_move = 2
    elif(choice=="end"):
        return
    else:
        clear()
        print("This is not a valid move. Please choose 'r', 'p', or 's'.")
        print_empty()
        game()
    ai_move = r.randint(0, 2)
    clear()
    determine_winner(player_move, ai_move)
    print_empty()
    game()

def determine_winner(a, b):
    if (a==0 and b==0 or a==1 and b==1 or a==2 and b==2):
        outcome(0)
    elif (a==0 and b==2 or a==1 and b==0 or a==2 and b==1):
        outcome(1)
    elif (a==0 and b==1 or a==1 and b==2 or a==2 and b==0):
        outcome(2)
    else:
        outcome(3)
        
def outcome(o):
    if (o == 0):
        print("Tie")
    elif (o==1):
        print("Player Wins")
    elif(o==2):
        print("AI Wins")
    else:
        print("Outcome Unknown")

def clear():
    #Clear console here
    os.system("cls")

def print_empty():
    print("")

game()