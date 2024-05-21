import unittest

class Solution:
    """
    LeetCode Problem 191: Number of 1 Bits
    Difficulty: Easy
    Topics: Bit Manipulation
    Time Complexity: O(1)
    Space Complexity: O(1)

    Write a function that takes a positive integer and returns the number of set bits
    (Hamming weight) in its binary representation.
    """

    def hammingWeight_1(self, n: int) -> int:
        """
        Key Ideas:
        - Iterate through each bit of the integer by right-shifting it by 1 in each iteration.
        - If the least significant bit is 1 (i.e., the result of n & 1 is 1), increment the result.

        Args:
        n (int): The input integer.

        Returns:
        int: The number of set bits in the binary representation of the integer.
        """
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight_2(self, n: int) -> int:
        """
        Count the number of set bits (1s) in the binary representation of the given integer using bitwise AND with n-1.

        Key Ideas:
        - Iterate through each set bit of the integer by using the expression n & (n - 1), which flips the least significant set bit to 0.
        - Increment the result for each set bit flipped to 0 until n becomes 0.

        Args:
        n (int): The input integer.

        Returns:
        int: The number of set bits in the binary representation of the integer.
        """
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome(self):
        self.assertEqual(self.solution.hammingWeight_1(11), 3)
        self.assertEqual(self.solution.hammingWeight_2(11), 3)

        self.assertEqual(self.solution.hammingWeight_1(128), 1)
        self.assertEqual(self.solution.hammingWeight_2(128), 1)

        self.assertEqual(self.solution.hammingWeight_1(2147483645), 30)
        self.assertEqual(self.solution.hammingWeight_2(2147483645), 30)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All test cases passed!")
