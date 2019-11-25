# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Rock Paper Scissors

# Make a two-player Rock-Paper-Scissors game.
# Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.
# Rock beats scissors 1-2 = -1
# Scissors beats paper 2-1= -1
# Paper beats rock    0-1= -1


# clear shell
def cls():
    print(50 * "\n")

# player choice
def player_choice(player):
    print("Player " + str(player) + ", what is your choice?")
       
    for i in range(0, len(tab)):
        print(str(i) + " - " + tab[i])

    choice=-1
    while choice not in ["0","1","2"]:
        choice=input("Enter 0, 1 or 2: ")
        
    print("\n")    
    return(choice)

# checking who is the winner
def check(pl1,pl2):
    if pl1==pl2:
        print("Nobody win!")
    elif pl1-pl2==-1:
        print("Player 1 win, because " + tab[pl1] + " beats " + tab[pl2] + "!")
    else:
        print("Player 2 win, because " + tab[pl2] + " beats " + tab[pl1] + "!")

# one players game
def one_player():
    player1=int(player_choice(1))
    player2=random.randint(0,2)
    
    print("Player1: ",tab[player1])    
    print("Player2 (computer): ",tab[player2])

    check(player1,player2)

# two players game
def two_players():
    player1=int(player_choice(1))
    player2=int(player_choice(2))

    print("Player 1: ",tab[player1])    
    print("Player 2: ",tab[player2])

    check(player1,player2)    

# main program

import random

tab=["paper", "rock", "scissors"]
new_game="y"
while new_game=="y":
    cls()

    print("Choose game mode.")
    print("1 - one player game")
    print("2 - two players game")
    game_type=0
    while game_type not in ["1","2"]:
        game_type=input("Enter 1 or 2: ")

    print("\n")
    
    if game_type=="2":
        two_players()
    else:
        one_player()

    print("\n")

    new_game=""
    while new_game!="y" and new_game!="n":
        new_game=input("Do you want to start a new game? (y/n)")

cls()
