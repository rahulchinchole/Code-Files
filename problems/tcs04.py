# Given an array with N-non negative integers and lower and upper limits
# R1 and R2 resp. Find the numbers R1<= NUM <=R2

from typing import Counter

def give_ele(req):
    Count = 0
    for i in range(len(x)):
        if i >= R1 and i <= R2:
            Count += 1
        
    print(Count)

# num = int(input("> "))
x = list(map(int, input().split()))
# print(x)

R1 = int(input("> "))
R2 = int(input("> "))

give_ele(x)