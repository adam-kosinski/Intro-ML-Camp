import sys
import math

def isprime(n):
    for i in range(1, math.ceil(math.sqrt(n)),2):
        if i == 1:
            i = 2
        if n%i == 0:
            return False

    return True


def primefac(n):
    facs = []
    i = 2
    while i <= n:
        print(i)
        if n%i==0 and isprime(i):
            n /= i
            print("n",n)
            facs.append(i)
            if isprime(n):
                facs.append(n)
                break
            i = 1
        i += 1
    print(facs)



def main():
    primefac(int(sys.argv[1]))

if __name__ == "__main__":
    main()