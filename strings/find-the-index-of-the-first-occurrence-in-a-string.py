import unittest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        LeetCode Problem 28: Implement strStr()
        Difficulty: Easy
        Topics: Two Pointers, String, String Matching

        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Key Ideas:
        - This is a basic string matching problem that can be solved using a brute-force approach.
        - Iterate through the haystack and check if each substring starting from the current index matches the needle.
        - If a match is found, return the current index; otherwise, return -1.

        Args:
        haystack (str): The input string to search in.
        needle (str): The substring to search for in the input string.

        Returns:
        int: The index of the first occurrence of the needle in the haystack, or -1 if the needle is not found.
        """

        length_needle = len(needle)

        for i in range(0, len(haystack) - length_needle + 1):
            j = 0
            while j < length_needle:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == length_needle:
                return i

        return -1

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_strStr(self):
        # Test case 1: Needle is present in haystack
        haystack = "hello"
        needle = "ll"
        self.assertEqual(self.solution.strStr(haystack, needle), 2)

        # Test case 2: Needle is not present in haystack
        haystack = "aaaaa"
        needle = "bba"
        self.assertEqual(self.solution.strStr(haystack, needle), -1)

        # Test case 3: Needle is an empty string
        haystack = "hello"
        needle = ""
        self.assertEqual(self.solution.strStr(haystack, needle), 0)

        # Test case 4: Needle and haystack are empty strings
        haystack = ""
        needle = ""
        self.assertEqual(self.solution.strStr(haystack, needle), 0)

        # Test case 5: Needle is longer than haystack
        haystack = "hi"
        needle = "hello"
        self.assertEqual(self.solution.strStr(haystack, needle), -1)

        # Test case 6: Needle is equal to haystack
        haystack = "hello"
        needle = "hello"
        self.assertEqual(self.solution.strStr(haystack, needle), 0)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
