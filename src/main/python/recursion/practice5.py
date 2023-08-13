# count the digits of a given number using recursion
def countDigit(n):
    if n == 0:
        return 0
    return 1 + countDigit(n // 10)


def countDigit2(n, count):
    if n != 0:
        count += 1
        count = countDigit2(n // 10, count)
    return count


print(countDigit(12345))
print(countDigit2(12345, 0))
