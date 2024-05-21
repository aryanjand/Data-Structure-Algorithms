import unittest

class Solution:
    def isUgly(self, n: int) -> bool:
        """
        LeetCode Problem 263: Ugly Number
        Difficulty: Easy
        Topics: Math
        Time Complexity: O(log N)
        Space Complexity: O(1)

        An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

        Given an integer n, return True if n is an ugly number, and False otherwise.

        Key Ideas:
        - If n is less than or equal to 0, it cannot be an ugly number.
        - Continuously divide n by 2, 3, and 5 as long as it is divisible by these numbers.
        - After removing all factors of 2, 3, and 5, if n is reduced to 1, it is an ugly number.

        """
        if n <= 0:
            return False

        for prime_number in [2, 3, 5]:
            while n % prime_number == 0:
                n = n // prime_number

        return n == 1


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isUgly(self):
        # Test case 1: Ugly number 6 (2 * 3)
        self.assertTrue(self.solution.isUgly(6))

        # Test case 2: Ugly number 8 (2^3)
        self.assertTrue(self.solution.isUgly(8))

        # Test case 3: Non-ugly number 14 (2 * 7)
        self.assertFalse(self.solution.isUgly(14))

        # Test case 4: Ugly number 1 (by definition)
        self.assertTrue(self.solution.isUgly(1))

        # Test case 5: Non-ugly number -6 (negative number)
        self.assertFalse(self.solution.isUgly(-6))

        # Test case 6: Non-ugly number 0
        self.assertFalse(self.solution.isUgly(0))

        # Test case 7: Ugly number 30 (2 * 3 * 5)
        self.assertTrue(self.solution.isUgly(30))

        # Test case 8: Large ugly number 1000 (2^3 * 5^3)
        self.assertTrue(self.solution.isUgly(1000))

        # Test case 9: Large non-ugly number 37 (prime number)
        self.assertFalse(self.solution.isUgly(37))
