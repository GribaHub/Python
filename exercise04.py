# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Divisors

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print(50 * "\n") # clear shell

print("*** A list of all the divisors of the number ***\n")
x=int(input("Number? "))

print()

div=[]
i=1
while i<=x:  
    if x % i==0:
        div.append(i)
        print(str(x) + " / " + str(i) + " = " + str(x/i))
    i=i+1

print()

print("Divisors of " + str(x) + ": ", end='')
print(div)

print()
