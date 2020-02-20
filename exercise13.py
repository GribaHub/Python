# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Fibonacci

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# 1, 1, 2, 3, 5, 8, 13, ...

# clear shell
def cls():
    print(50 * "\n")

# Fibonnaci
def fib(l):
    result=[]
    x=1
    y=0
    for i in l:
        z=x+y
        result.append(z)
        x=y 
        y=z
    return(result)
  
# main program

cls()

i=int(input("How many Fibonnaci numbers to generate? "))

list=range(1,i+1)
print("Fibonnaci numbers: ",fib(list))
