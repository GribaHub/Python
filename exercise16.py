# Beginner Python exercises

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# clear shell
def cls():
    print(50 * "\n")

def ascii_check():
    # A - Z
    for i in range(26):
        print(i+65," - ",chr(i+65))

    print()

    # a - z
    for i in range(26):
        print(i+97," - ",chr(i+97))

    print()

    # 0 - 9
    for i in range(10):
        print(i+48," - ",chr(i+48))

    print()

    # special
    for i in range(15):
        print(i+33," - ",chr(i+33))

    print()

    # special2
    for i in range(7):
        print(i+58," - ",chr(i+58))

# pass example

def passw1(passlen):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p =  "".join(random.sample(s,passlen ))
    return(p)

# my pass

def passw2(passlen):
    p=[]
    for i in range(passlen):
        p.append(random.randint(0,4))

    passw=[]

    for i in p:
        if i==0: passw.append(chr(random.randint(65,65+26)))
        if i==1: passw.append(chr(random.randint(97,97+26)))
        if i==2: passw.append(chr(random.randint(48,48+10)))
        if i==3: passw.append(chr(random.randint(33,33+15)))
        if i==4: passw.append(chr(random.randint(58,58+7)))

    return("".join(passw))

# main program

import random

cls()

#ascii_check()

for i in range(10):
    print(">",passw2(8),"<")
