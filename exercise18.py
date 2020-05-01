# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull”.
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

# clear shell
def cls():
    print(50 * "\n")

# the game
def game(nr):
    # checking if user input number and the number is in (1000-9999)
    unr = 1              
    while (unr < 1000) or (unr > 9999):
        unrtxt = input("Give me a 4-digit number (1000-9999) or press enter for quit: ")
        if unrtxt == "": break
        unr = 1
        for i in unrtxt:
            if i not in ch: unr = 0
        if unr != 0: unr = int(unrtxt)

    # counting cows and bulls
    if unrtxt != "":
        nrtemp=[]
        for i in range(4): nrtemp.append(nr[i])

        cows = 0
        for i in range(0,4):
            if nrtemp[i] == unrtxt[i]:
                cows = cows + 1
                nrtemp[i] = "x"

        bulls=0

        for i in range(0,4):
            for j in range(0,4):
                if nrtemp[i] == unrtxt[j]:
                    nrtemp[i] = "x"
                    bulls = bulls + 1
            
        print("Cows:",cows)
        print("Bulls:",bulls)
        print()

        # checking if user win
        if cows == 4:
            print("************\n* You win! *\n************\n")
            print("Number of guesses:", itr)
            unrtxt=""
    else: print("\nThe number was:","".join(nr))

    return unrtxt

# generating number (1000-9999) with different digits
def gen1():
    nrg = []
    nrg.append(str(random.randint(1,9)))
    while len(nrg) < 4:
        rnd=str(random.randint(0,9))
        if rnd not in nrg: nrg.append(rnd)

#    print(nrg)

    return(nrg)

# generating number (1000-9999) (possible same digits)
def gen2():
    nrg = []
    nrg.append(str(random.randint(1,9)))
    for i in range(3): nrg.append(str(random.randint(0,9)))

#    print(nrg)

    return(nrg)

# main program
cls()

print('For every digit that the user guessed correctly in the correct place, they have a “cow”.')
print('For every digit the user guessed correctly in the wrong place is a “bull".\n')

# preparing global variable 'ch' with digits as string
ch = []
for i in range(10):
    ch.append(str(i))

nrgn = gen1()

itr = 1
while game(nrgn) != "": itr += 1
