# finds all numbers x whose crosssum is the same number as x / 13
# since the biggest number a crosssum can be is 36, x / 13 may also only be 36 or lower -> 13 * 36 = 468
# all numbers msut be a multiple of 13 since x / 13 has to provide an int. 

def main():

    numbers = []
    solutions = []

    for i in range(13, 468, 13):
        numbers.append(i)

    for number in numbers:
        if (crosssum(number) == number / 13):
         solutions.append(number)

    if solutions == None:
        print("No results found")

    else:
        for solution in solutions:
            print(solution)

def crosssum(n):
   c = 0
   while n:
       c, n = c + n % 10, n // 10
   return c

if __name__ == "__main__":
    main()