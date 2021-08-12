# METHOD 1
# def rightRotateByOne(A):
#     last = A[-1]
#     for i in reversed(range(len(A)-1)):
#         A[i+1] = A[i]
    
#     A[0] = last


# def rightRotate(A, k):
#     for i in range(k):
#         rightRotateByOne(A)

# n = int(input())
# A = []

# for i in range(n):
#     a = int(input("> "))
#     A.append(a)
    
# # print(len(A))
# k = int(input())

# rightRotate(A, k)

# for i in range(n):
#     print(A[i], end=" ")

# METHOD 2 
def rotate_print(x, k):
    for i in range(len(x)):
        # print(x[(i+k) % len(x)], end=" ") 
        print(x[(i-(k)) % len(x)], end=" ")
        # print(x[(i-(k)) % len(x)], end=" ")


n = int(input())
x = list(map(int, input().split()))
k = int(input())

# print(x)

rotate_print(x, k) 


