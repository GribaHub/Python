# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Rock Paper Scissors

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# 
# Keep the game going until the user types “exit”.
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# clear shell
def cls():
    print(50 * "\n")

# user answer and check
def game(sh):
    usr_num=0
    while usr_num not in range(1,10):
        usr_num=input("Enter number (1-9) or 'exit': ")
        if usr_num=="exit":
            print("You quit after",str(sh),"gusses!")
            return(1)
        usr_num=int(usr_num)
        
    if usr_num>ran_num:
        print("Your number is too high! Try again.")
        return(0)
    elif usr_num<ran_num:
        print("Your number is too low! Try again.")
        return(0)
    else:
        print("You win after",str(sh+1),"gusses! The number was",str(ran_num),".")
        return(1)
    
# main program

import random

cls()

ran_num=random.randint(1,9)

print("Try to find random number between 1 and 9 (including 1 and 9).")

shots=0
end=0
while end!=1:
    end=game(shots)
    shots=shots+1
