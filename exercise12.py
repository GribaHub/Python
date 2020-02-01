# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# List Ends

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

# clear shell
def cls():
    print(50 * "\n")

# function
def new_list(list):
    b=[]

    b.append(a[0])
    b.append(a[len(a)-1])

    return(b)

# main program

cls()

a = [5, 10, 15, 20, 25]

print(new_list(a))
