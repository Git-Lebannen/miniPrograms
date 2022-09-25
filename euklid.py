import sys
import math

def main():

    usage = ("Usage: python euklid.py <number 1> <number 2> (<-s>: list steps). Euklid.py will return the largest common divider. It will not accept decimal numbers.")
    
    # check the given command line args
    argc = len(sys.argv)
    if argc > 3 or argc == 2 or argc == 1:
        print(usage)
        quit()

    # convert command line args to ints, check value errors
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print(usage)
        quit() 

    # set number variables according to size 
    if num1 > num2:
        a = num1
        b = num2
    else:
        a = num2
        b = num1

    r = 1
    lastR = r

    while r != 0:
        lastR = r
        r = a % b
        a = b
        b = r 

    print(lastR)

if __name__ == "__main__":
    main()