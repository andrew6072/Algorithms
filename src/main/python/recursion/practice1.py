# Write a program to print the first 50 natural numbers using recursion.


def printNum(n):  # this function prints numbers from 1 to n
    if n < 1:
        return
    printNum(n - 1)
    print(n)


# printNum(50)

# another way: print from n to 50
def printNum2(n):
    if n <= 50:
        print(n)
        printNum2(n + 1)


printNum2(25)
