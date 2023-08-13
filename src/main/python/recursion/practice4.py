# print the array elements using recursion


def printArray(a, i):
    if i < len(a):
        print(a[i], end=" ")
        printArray(a, i + 1)


def printArray2(a, i):
    if i < 0:
        return
    printArray2(a, i - 1)
    print(a[i], end=" ")


a = [2, 4, 6, 8, 10, 12]
printArray(a, 0)
print()
printArray2(a, len(a) - 1)
