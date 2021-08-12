
# number = int(input("Enter Number: "))
# factorial = 1

# if number < 0 :
#     print("Factorial does not exits for negative numbers")
# elif number == 0 :
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1, number+1):
#         factorial = factorial * i
#     print(str(factorial))


def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
num = 5  
print("Factorial of",num,"is",)  
fact(num)  