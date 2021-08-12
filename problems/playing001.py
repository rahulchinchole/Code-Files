# Get a name as input 
# From the length of that input/'name' decide how many digits could be in the 'list'
# count- for counting the total numbers, btw this is nor necessary here, 
# because you can directly say from 'name' how many digits are there! 
# take inputs of elements = len(name) 
# appended to the list
# printed the list (#1)
# making this more interesting now :)
# if user wants to sort their list give them a sorted list otherwise print 'Its Okay, No Problem' (#2)



name = input("Enter Your name: ")
print("You can add max " + str(len(name))+ " Digits in Array")
count = 1
for i in range(len(name)):
    # print(str(count) + " number")
    lst = list(map(int, input().split()))
    count = count + 1

print(lst)
print("Total Digits in Array:" + str(count))

print("You wanna sored list? (Yes/No)")
response = input("> ")

if response == "Yes":
    # sortedList = lst.sort()
    print(sorted(lst))
else:
    print("Okay,"+ str(name) + " No problem!")
    print(lst)
