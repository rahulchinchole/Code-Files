P = int(input("> "))

def check(P, k):
    if P <= 0:
        return 0
    else:
        k = P/4
        # print(k)
    
    print("SEC A WILL GET: " + str(k))
    print("SEC B WILL GET: " + str(k))
    print("SEC C WILL GET: " + str(k))
    print("SEC D WILL GET: " + str(k))

check(P)