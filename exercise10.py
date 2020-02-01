# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# List Overlap Comprehensions

# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes. 

# clear shell
def cls():
    print(50 * "\n")

# main program

cls()

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

# Solution with comprehensions.
common = [x for x in a if (x in b)]

# It doesn't work, because variable value is not changing inside comprehensions.
# common = [x for x in a if ((x in b) and (x not in common))]

# Solution (good and simple, no duplicates) without comprehensions.
#for x in a:
#    if x in b:
#        if x not in common:
#            common.append(x)

print("a =",a)
print("b = ",b)
print()

print("Solution with duplicates: ", end='')
print(common)

print("Solution without duplicates: ", end='')
print(list(set(common)))

# Test of conditions
# print((1 in b) and (1 not in common))
