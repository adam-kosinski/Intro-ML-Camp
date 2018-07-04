import sys
import math

def isprime(n):
    for i in range(1, math.ceil(math.sqrt(n)),2):
        if i == 1:
            i = 2
        if n%i == 0:
            print(n,"is divisible by",i,"=",n/i)
            return

    print(n, "is prime")


def main():
    isprime(int(sys.argv[1]))

if __name__ == "__main__":
    main()