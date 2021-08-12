# Q1. Write a program to find the count of numbers that consists of unique digits.

# Input:
# Input consists of two Integer lower and upper value of a range
# Output:
# The output consists of a single line, print the count of unique digits in a given range. 
# Else Print"No Unique Number"



# main finction of the code to know whether the digits repeates Or not!
def repeated_digits(n):
    a = []
    while n != 0:
        d = n % 10
        if d in a:
            return 0
        a.append(d)
        n = n // 10
    return 1

# runs a function to get increment
def unique(num1, num2):
    ans = 0
    for i in range(num1, num2+1):
        ans = ans + repeated_digits(i)
    return ans

# takes inputs
num1, num2 = int(input()), int(input())
print(unique(num1, num2))


    
