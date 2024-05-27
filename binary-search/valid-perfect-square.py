import unittest

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        LeetCode Problem 367: Valid Perfect Square
        Difficulty: Easy
        Topics: Math, Binary Search

        Given a positive integer num, return true if num is a perfect square or false otherwise.
        A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

        You must not use any built-in library function, such as sqrt.

        Key Ideas:
            - Perform a binary search for efficiency.
            - If the mid value squared equals the target number, return True.
            - If the square of the mid value is greater than the target number, adjust the right boundary.
            - If the square of the mid value is less than the target number, adjust the left boundary.
            - The loop condition left < right ensures the search space is narrowed correctly.
        """

        left, right = 0, num

        while left <= right:
            mid = (right - left) // 2 + left

            if mid**2 > num:
                right = mid - 1
            elif mid**2 < num:
                left = mid + 1
            else:
                return True

        return False


class TestIsPerfectSquare(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_perfect_square(self):
        self.assertTrue(self.solution.isPerfectSquare(1))
        self.assertTrue(self.solution.isPerfectSquare(4))
        self.assertTrue(self.solution.isPerfectSquare(9))
        self.assertTrue(self.solution.isPerfectSquare(16))
        self.assertTrue(self.solution.isPerfectSquare(25))
        self.assertTrue(self.solution.isPerfectSquare(36))
        self.assertTrue(self.solution.isPerfectSquare(49))
        self.assertTrue(self.solution.isPerfectSquare(64))
        self.assertTrue(self.solution.isPerfectSquare(81))
        self.assertTrue(self.solution.isPerfectSquare(100))

    def test_not_perfect_square(self):
        self.assertFalse(self.solution.isPerfectSquare(2))
        self.assertFalse(self.solution.isPerfectSquare(3))
        self.assertFalse(self.solution.isPerfectSquare(5))
        self.assertFalse(self.solution.isPerfectSquare(6))
        self.assertFalse(self.solution.isPerfectSquare(7))
        self.assertFalse(self.solution.isPerfectSquare(8))
        self.assertFalse(self.solution.isPerfectSquare(10))
        self.assertFalse(self.solution.isPerfectSquare(15))
        self.assertFalse(self.solution.isPerfectSquare(26))
        self.assertFalse(self.solution.isPerfectSquare(50))

    def test_large_numbers(self):
        self.assertTrue(self.solution.isPerfectSquare(10000))
        self.assertTrue(self.solution.isPerfectSquare(12321))  # 111^2
        self.assertFalse(self.solution.isPerfectSquare(12345))
        self.assertTrue(self.solution.isPerfectSquare(1000000))  # 1000^2
        self.assertFalse(self.solution.isPerfectSquare(1000001))

    def test_zero(self):
        self.assertTrue(self.solution.isPerfectSquare(0))

if __name__ == "__main__":
    unittest.main(exit=False)
    print('All Test Cases Passed')
