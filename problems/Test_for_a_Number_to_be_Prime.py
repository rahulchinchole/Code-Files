# Let p be a given number and let n be the smallest counting number such that n2 ≥ p.
# Now, test whether p is divisible by any of the prime numbers less than or equal to n. If yes, then p is not
# prime otherwise, p is prime.

p = int(input("Number: "))

if p > 1:
    for i in range(2, p):
        if ( p % i == 0):
            print("Not A Prime Number")
            break
    else:
        print("Prime Number!")
else:
    print("not a prime number!")
