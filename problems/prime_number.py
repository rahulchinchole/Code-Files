#  Python Program to Check Prime Number

num = int(input("Enter the number: "))

if num > 1:
    for i in range(2, num):
        if ( num %  i) == 0:
            print(num, "is Not a Prime Number.")
            break
    else :
        print(num, "is a Prime Number")

else:
    print(num, "is Not a Prime Number")
