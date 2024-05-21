import unittest

class Solution:
    def isAlphanumeric(self, c: str) -> bool:
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')

    def isPalindrome(self, s: str) -> bool:
        """
        LeetCode Problem: Valid Palindrome
        Difficulty: Easy
        Topics: String, Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)

        Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        A palindrome is a string that reads the same forward and backward.

        Key Ideas:
        - Use two pointers to compare characters from both ends of the string.
        - Ignore non-alphanumeric characters by skipping them with the help of the isAlphanumeric helper method.
        - Convert characters to lower case to ensure the comparison is case-insensitive.
        - If all the corresponding characters from both ends match, return True; otherwise, return False.
        """
        length_s = len(s)
        left, right = 0, length_s - 1

        while left <= right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while left < right and not self.isAlphanumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome(self):

        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama!")) # True

        self.assertFalse(self.solution.isPalindrome("race a car")) # False

        self.assertTrue(self.solution.isPalindrome("RAce    Car")) # True

        self.assertTrue(self.solution.isPalindrome(".[;.[;,;.][;;';.';.")) # Ture


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All test cases passed!")
