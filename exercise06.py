# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# String Lists

# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# clear shell
def cls():
    print(50 * "\n")

# main program

cls()

text=input("Enter text: ")

i=len(text)-1
mirror=""

while i>=0:
    mirror=mirror+text[i]
    i=i-1

if text==mirror:
    print("This is a PALINDROME! " + text + "=" + mirror)
else:
    print("This is not a PALINDROME! " + text + "<>" + mirror)

