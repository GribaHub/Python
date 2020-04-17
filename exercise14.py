# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

# clear shell
def cls():
    print(50 * "\n")

# function using sets
def no_dup_sets(list):
    return(set(list))

# function using loop
def no_dup_loop(list):
    result=[]

    for i in list:
        test=0
        for j in result:
            if j==i:
                test=1
        if test==0:
            result.append(i)
           
    return(result)

# function using loop (better solution)
def no_dup_loop2(list):
    result=[]

    for i in list:
        if i not in result:
            result.append(i)
           
    return(result)

# main program

cls()

a = [1, 1, 2, 3, 5, 8, 1, 3, 2, 2, 2]

print(a)
print(no_dup_sets(a)) # Calling function with sets.
print(no_dup_loop(a)) # Calling function with loop.
print(no_dup_loop2(a)) # Calling function with loop (better solution).
