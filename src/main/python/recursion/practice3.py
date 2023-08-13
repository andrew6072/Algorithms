def valFibonacci(n):  # n must >= 1
    if n == 2:
        return 1
    if n == 1:
        return 1
    return valFibonacci(n - 1) + valFibonacci(n - 2)


def printFibonacci(n):
    for i in range(1, n + 1):
        print(valFibonacci(i), end=" ")


printFibonacci(10)
