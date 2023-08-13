# calculate the sum of numbers from 1 to n using recursion
import unittest


def calSum(n):
    if n < 1:
        return 0
    return n + calSum(n - 1)


def loopSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


class TestSumFunction(unittest.TestCase):
    def test_10(self):
        self.assertEquals(calSum(10), loopSum(10))

    def test_1(self):
        self.assertEquals(calSum(1), loopSum(1))

    def test_100(self):
        self.assertEquals(calSum(100), loopSum(100))
