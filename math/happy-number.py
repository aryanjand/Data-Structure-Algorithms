import unittest

class Solution:
    def isHappy(self, n: int) -> bool:
        visted = set()

        while n != 1:
            if n in visted:
                return False
            visted.add(n)
            res = 0

            while n:
                res = res + (n % 10)**2
                n = n // 10
            n = res

        return True


class TestSolution(unittest.TestCase):
    def __init__(self):
        self.solution = Solution()

    def test_isHappy(self):
        self.assertTrue(self.solution.isHappy(19))  # 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1
        self.assertFalse(self.solution.isHappy(2))  # 2^2 = 4, 4^2 = 16, 1^2 + 6^2 = 37, 3^2 + 7^2 = 58, 5^2 + 8^2 = 89, 8^2 + 9^2 = 145, 1^2 + 4^2 + 5^2 = 42, 4^2 + 2^2 = 20, 2^2 + 0^2 = 4 (cycle)
        self.assertTrue(self.solution.isHappy(7))   # 7^2 = 49, 4^2 + 9^2 = 97, 9^2 + 7^2 = 130, 1^2 + 3^2 + 0^2 = 10, 1^2 + 0^2 = 1

if __name__ == '__main__':
    TestSolution().test_isHappy()
    print("All Test Cases Passed!")
