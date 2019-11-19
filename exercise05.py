# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# List Overlap

# Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Randomly generate two lists to test this.

# clear shell
def cls():
    print(50 * "\n")

# generate random list
def random_tab(tab_length,min_value,max_value):
    tab=[]
    i=1
    while i<=tab_length:
        tab.append(random.randint(min_value,max_value))
        i=i+1
    return(tab)

# main program

import random

cls()

tab1=random_tab(random.randint(1,10),1,10)
tab2=random_tab(random.randint(1,10),1,20)

print("List 1: ", end='')
print(tab1)

print("List 2: ", end='')
print(tab2)

tab3=[]

for i in tab1:
    if i in tab2:
        if i not in tab3:
            tab3.append(i)

if tab3!=[]:
    print("List that contains only the elements that are common between the lists (without duplicates): ", end='')
    print(tab3)
else:
    print("List is empty! No common elements between the lists.")
