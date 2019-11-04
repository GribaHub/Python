# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Odd or Even
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

answer="y"

while answer=="y":
    x=input("Enter a number: ")
    print("You entered number: " + x)
    x=int(x)
    if x % 2==0:
        print("This is even number.")
        if x % 4==0 : print("The number is divisible by 4.")
    else:
        print("This is odd number.")
    
    answer=""
    while answer!="y" and answer!="n":
        answer=input("Again? (y/n): ")

print("End of the program! Your answer: " + answer)
