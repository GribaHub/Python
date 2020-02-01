# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Check Primality Functions

# Ask the user for a number and determine whether the number is prime or not.

# clear shell
def cls():
    print(50 * "\n")

# check if the number is prime or not
def check(num):
    if num==1:
        return("not")
    seq=range(2,num)
    for i in seq:
        print(num," % ",i," = ",num%i)
        if num%i==0:          
            return("not")
    return("")

# main program

cls()

usr_num=int(input("Enter number: "))

print(usr_num,"is",check(usr_num),"the prime number!")
