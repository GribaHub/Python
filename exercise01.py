# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# 1. Character Input
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Solution by Piotr 'Griba' Grzybowski

name=input("What is your name? ")

name_end=name[len(name)-1]

print("This is probably ", end='');

# Usually in polish (with some exceptions), women names are ending with "a".
if name_end!="a":
    print("male name!")
elif name=="Griba" or name=="Kuba":
    print("male name!") 
else:
    print("female name!")

age=int(input("How old are you? "))

import datetime
now = datetime.datetime.now()
year = now.year

print(name + ", in " + str(100-age+year) + " you", end='')

if age==100:
    print(" are ", end='')
else:
    print(" will be ", end='') if age<100 else print(" was ", end='')

print("100 years old!")

print("")
num=int(input("Give me a number: "))
print(num * ("Hello " + name + "!\n"))
