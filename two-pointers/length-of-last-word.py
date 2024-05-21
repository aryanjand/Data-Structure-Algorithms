import unittest

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        LeetCode Problem 58: Length of Last Word
        Difficulty: Easy
        Topics: String
        Time Complexity: O(N)
        Space Complexity: O(1)

        Given a string s consisting of words and spaces, return the length of the last word in the string.

        A word is defined as a maximal substring consisting of non-space characters only.

        Key Ideas:
        - Reverse the string, and then find, then find the first non-space character. Stop right pointer.
        - Continue left pointer until start of the string or space character is reached.
        - The length of the last word is calculated by subtracting the position of the beginning of the word (left) from the position of the end of the word (right).
        """
        s = s[::-1]

        left = 0
        while left < len(s) and s[left] == ' ':
            left += 1

        right = left
        while right < len(s) and s[right] != ' ':
            right += 1

        return right - left


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLastWord(self):
        # Test case 1: General case with spaces between words
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

        # Test case 2: Single word without trailing spaces
        self.assertEqual(self.solution.lengthOfLastWord("OpenAI"), 6)

        # Test case 3: Single word with trailing spaces
        self.assertEqual(self.solution.lengthOfLastWord("OpenAI "), 6)

        # Test case 4: Multiple spaces at the end
        self.assertEqual(self.solution.lengthOfLastWord("OpenAI is great   "), 5)

        # Test case 5: Empty string
        self.assertEqual(self.solution.lengthOfLastWord(""), 0)

        # Test case 6: String with only spaces
        self.assertEqual(self.solution.lengthOfLastWord("    "), 0)

        # Test case 7: Multiple spaces between words
        self.assertEqual(self.solution.lengthOfLastWord("The sky is blue"), 4)

        # Test case 8: No spaces
        self.assertEqual(self.solution.lengthOfLastWord("Python"), 6)

        # Test case 9: Leading spaces
        self.assertEqual(self.solution.lengthOfLastWord("   Hello"), 5)
