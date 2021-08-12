# Program to swap two numbers without using the third variable
# Taking input from users, using function, swapping, concatation of str and int : all in one small programme

val1 = input("Enter First Value: ")
val2 = input("Enter Second Value: ")


def swapping(a, b):
    print("before swapping: a and b are ", str(a), str(b), " respectively")
    a, b = b, a
    print ("now a: ", str(a), " b: ", str(b))
 

swapping(val1, val2)

