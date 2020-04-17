# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

# clear shell
def cls():
    print(50 * "\n")

# backwards order (loop)
def backwards(text):
    result=text.split(" ")

    lnth=len(result)
    j=range(lnth)
    text=[]
    for i in j:
        text.append(result[lnth-i-1])

    result=[]
    result=" ".join(text)
    return(result)

# backwards order (reverse)
def backwards2(text):
    result=text.split(" ")
    result.reverse()
    result=" ".join(result)
    return(result)

# main program

cls()

print("Words in backwards order:",backwards(input("Enter a string containing multiple words: ")))
print()
print("Words in backwards order:",backwards2(input("Enter a string containing multiple words: ")))
