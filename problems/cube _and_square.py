
# write a code which gives square of number if it's Even and cube if it's an Odd

number_ = int(input("Enter Number: "))

if number_ % 2 == 0:
    print("Square of " + str(number_) + " is: " + str(number_ ** 2))
else:
    print("Cube of " + str(number_) + " is: " + str(number_ * number_* number_))


