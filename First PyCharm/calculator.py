import sys
import math


def pythag(a,b):
    return (a**2 + b**2) ** .5


def main():

    whatToDo = ""

    if len(sys.argv) >= 2:
        whatToDo = sys.argv[1]


    if whatToDo == "add":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x+y)
    elif whatToDo == "sub":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x-y)
    elif whatToDo == "mul":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x*y)
    elif whatToDo == "div":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x/y)
    elif whatToDo == "mod":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x%y)
    elif whatToDo == "pow":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x**y)
    elif whatToDo == "countTo":
        x = int(sys.argv[2])
        for i in range(x+1):
            print(i)
    elif whatToDo == "pythag":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(pythag(x,y))
    elif whatToDo == "repeat":
        string = sys.argv[2];
        for i in range(int(sys.argv[3])):
            print(string)


if __name__ == "__main__":
    main()
