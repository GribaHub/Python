# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# List less than ten

# Write a program that prints out all the elements of the list that are less than 5.

some_nr=[11, 1, 23, 3, 5, 8, 13, 21, 34, 55, 89]
solution=[]

for x in some_nr:
    if x<10:      
        solution.append(x)

print("From ", end='')
print(some_nr, end='')
print(" less than 10 are ", end='')
print(solution, end='')
print(".")
