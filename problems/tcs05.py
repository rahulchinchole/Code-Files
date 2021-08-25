# if sum of all the numbers from a list is 0, print 1 else 0

Arr = []

N = int(input("N "))
count = 0

for i in range(0, N):
    ele = int(input("> "))
    Arr.append(ele)
    count += ele

# print(count)

if count == 0:
    print(1)
else:
    print(0)