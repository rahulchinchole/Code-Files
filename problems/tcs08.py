from typing import Counter
a = []
b = int(input())

count = 0
for i in range(b):
    k = int(input())
    count = count + k
    a.append(k)
    
# print(sorted(a))
# print(count)

dig = count - a[-1]
# print(dig)

if (a[-1] - 30) <= dig:
    print("success")
else:
    print("no")


