# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# List Comprehensions

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# clear shell
def cls():
    print(50 * "\n")

# search even elements by while
def search1(a):
    x=len(a)
    even_list=[]
    i=0
    while i<x:
        if a[i] % 2 == 0:
            even_list.append(a[i])
        i=i+1
    return(even_list)
    
# search even elements by for
def search2(a):
    even_list=[]
    for i in range(len(a)):
        if a[i] % 2 == 0:
            even_list.append(a[i])
    return(even_list)

# search even elements by list comprehension - don't like this!
def search3(a):
    even_list=[x for x in a if x % 2 == 0]
    return(even_list)

# main program

import datetime

cls()
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 140, 190, 220, 234, 255, 333, 456, 478, 490] # I put here more arguments than in example.

print("List of elements: ", end="")
print(a)
print("\n")

print("List of even elements (by WHILE): ", end="")

now = datetime.datetime.now()
sec1=now.microsecond
print(search1(a))
now = datetime.datetime.now()
sec2=now.microsecond
print("Operation took " + str(sec2-sec1) + " μs.") # Because I was interested how fast is Python I put this line here.

print("\n")

print("List of even elements (by FOR): ", end="")

now = datetime.datetime.now()
sec1=now.microsecond
print(search2(a))
now = datetime.datetime.now()
sec2=now.microsecond
print("Operation took " + str(sec2-sec1) + " μs.") # Because I was interested how fast is Python I put this line here.


print("\n")

print("List of even elements (by LIST COMPREHENSION): ", end="")

now = datetime.datetime.now()
sec1=now.microsecond
print(search3(a))
now = datetime.datetime.now()
sec2=now.microsecond
print("Operation took " + str(sec2-sec1) + " μs.") # Because I was interested how fast is Python I put this line here.
