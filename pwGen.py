# 'hash' function for password creation

# imports
import sys

# constants

# Pi decimals, with offset for 1-indexing
PIDECS = ['offset', 1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,
        2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,
        6,9,3,9,9,3,7,5,1,0,5,8,2,0,9,7,4,9,4,4,
        5,9,2,3,0,7,8,1,6,4,0,6,2,8,6,2,0,8,9,9,
        8,6,2,8,0,3,4,8,2,5,3,4,2,1,1,7,0,6,7,9,
        8,2,1,4,8,0,8,6,5,1,3,2,8,2,3,0,6,6,4,7,
        0,9,3,8,4,4,6,0,9,5,5,0,5,8,2,2,3,1,7,2,
        5,3,5,9,4,0,8,1]

# main function
def main():

    # var for length input
    adjusted = False

    # var for result print
    input = False

    # password var for result print
    password = ''

    # usage print
    print("""
----------------------------------------------------------------------
Usage:
python passwordGen.py <key> <(int) length !1>

!1 
Default is 8, Minimum is 5 and Maximum is 16.
Inputs that exceed these boundaries will be adjusted automatically.
----------------------------------------------------------------------
    """)

    # arg handling
    if len(sys.argv) - 1 <= 2:

        # with length input (valid or not)
        try:
            length = int(sys.argv[2])
            
            # length input clamping
            if length < 5:
                length = 5
                adjusted = True
            elif length > 16:
                length = 16
                adjusted = True

            input = True

            # password gen with given (possibly adjusted) length
            password = generatePassword(sys.argv[1], length)

        # without lenght input
        except (ValueError, IndexError):

            # password gen with standard length (= 8)
            password = generatePassword(sys.argv[1], 8)

        # results print
        adjustPrint = ('\033[F\033[F', 'Your length input was adjusted.')[adjusted]
        lengthArgPrint = ('No length argument provided.', '\033[F\033[F' )[input]

        print(f"""
----------------------------------------------------------------------
Results:

{password}

{adjustPrint}

{lengthArgPrint}
----------------------------------------------------------------------
            """, end = '')

    # invalid args        
    else:
        print('\nInvalid input')

# password gen, depends on key and length
def generatePassword(key, length):

    # create keySum by checking all indicies of the key string
    keySum = 0

    for var in key:

        # int handling
        try:
            val = int(var)
            keySum += (10 - val)

        # char handling
        except ValueError:

            val = ord(var)

            # lowercase chars add their 1-indexed value in the alphabet
            if val > 90:
                keySum += val - 96

            # uppercase chars add twice their 1-indexed value in the alphabet
            else:
                keySum += (val - 64) * 2

    # third password component 
    decimals = list(map(int, str(1 / keySum).split('.')[1]))

    for i, val in enumerate(decimals):
        if val > 0:
            comp3 = str(decimals[i]) + str(decimals[i + 1])
            break

    # first password component
    comp1 = int(comp3[0]) + int(comp3[1])

    # second password component 
    comp2 = PIDECS[int(comp3)]

    # password assembly
    password = [0] * length
    password[0] = (comp1, comp1 // 10)[comp1 >= 10]
    password[1] = comp2
    password[2] = int(comp3[0])
    password[3] = int(comp3[1])

    i = 0
    for j in range(4, len(password)):
        password[j] = PIDECS[comp1 + 1 + i]
        i += 1

    return password

# run main
if __name__ == "__main__":
    main()