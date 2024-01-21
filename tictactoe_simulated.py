import random as r
import os
import csv
import matplotlib.pyplot as plt

player_move = 0
ai_move = 0
iterations = 0

ties = 0
wins_ai1 = 0
wins_ai2 = 0

xval_list = []
winslist_ai1 = []
winslist_ai2 = []
winslist_ties = []

filelocat = "data.csv"
fieldnames = ['ai1_wins', 'ai2_wins', 'ties']

with open(filelocat, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

iterations = int(input("How many iterations should be simulated? | Iterations: "))
if (iterations <= 0):
    iterations = 1

def game():
    player_move = r.randint(0, 2)
    ai_move = r.randint(0, 2)
    determine_winner(player_move, ai_move)
    print_empty()

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
    global ties
    global wins_ai1
    global wins_ai2
    if (o == 0):
        print("Tie")
        ties=ties+1
    elif (o==1):
        print("AI 1 Wins")
        wins_ai1=wins_ai1+1
    elif(o==2):
        print("AI 2 Wins")
        wins_ai2=wins_ai2+1
    else:
        print("Outcome Unknown")
    with open(filelocat, 'a', newline='') as csvfile:
        fieldnames = ['ai1_wins', 'ai2_wins', 'ties']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'ai1_wins': wins_ai1, 'ai2_wins': wins_ai2, 'ties': ties})
    
def organize_data():
    global winslist_ai1
    global winslist_ai2
    global winslist_ties
    with open(filelocat, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rownum = 0
        for row in spamreader:
            if (rownum==0):
                winslist_ai1.append(row)
            elif (rownum==1):
                winslist_ai2.append(row)
            else:
                ties.append(row)
            rownum+=1

def graph_data():
    global xval_list
    it = 0
    for i in range(len(winslist_ai1)):
        xval_list.append(it)
        it+=1
    plt.plot(xval_list, winslist_ai1)
    plt.plot(xval_list, winslist_ai2)
    plt.plot(xval_list, winslist_ties)

def clear():
    #Clear console here
    os.system("cls")

def print_empty():
    print("")

for i in range(iterations):
    game()

organize_data()
graph_data()

plt.show()