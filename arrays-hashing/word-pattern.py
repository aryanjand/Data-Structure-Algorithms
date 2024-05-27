import unittest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        LeetCode Problem 290: Word Pattern
        Difficulty: Easy
        Topics: String, Hash Tables
        Time Complexity: O(N + M)
        Space Complexity: O(N + M)

        Given a pattern and a string s, determine if s follows the same pattern.
        Here, "follows" means there is a bijection between a letter in the pattern and a non-empty word in s.

        Constraints:
            s does not contain any leading or trailing spaces.
            All the words in s are separated by a single space.

        Key Ideas:
            - We need to create a mapping from pattern to string and from string to pattern. This ensures that each pattern
              character uniquely maps to a specific word in the string and vice versa.
            - It is beneficial to build the list (array) of words from the string beforehand to facilitate the mapping process.
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapPS = {}
        mapSP = {}

        for char, word in zip(pattern, words):
            if char in mapPS:
                if mapPS[char] != word:
                    return False
            else:
                mapPS[char] = word

            if word in mapSP:
                if mapSP[word] != char:
                    return False
            else:
                mapSP[word] = char

        return True

class TestWordPattern(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()


    def test_pattern_matches(self):
        self.assertTrue(self.solution.wordPattern("abba", "dog cat cat dog"))
        self.assertTrue(self.solution.wordPattern("abcd", "dog cat mouse bird"))
        self.assertTrue(self.solution.wordPattern("a", "dog"))

    def test_pattern_does_not_match(self):
        self.assertFalse(self.solution.wordPattern("abba", "dog cat cat fish"))
        self.assertFalse(self.solution.wordPattern("aaaa", "dog cat cat dog"))
        self.assertFalse(self.solution.wordPattern("abba", "dog dog dog dog"))

    def test_pattern_and_words_length_mismatch(self):
        self.assertFalse(self.solution.wordPattern("abc", "dog cat"))
        self.assertFalse(self.solution.wordPattern("a", "dog cat"))
        self.assertFalse(self.solution.wordPattern("ab", "dog"))

    def test_empty_pattern_and_string(self):
        self.assertTrue(self.solution.wordPattern("", ""))

    def test_empty_pattern_or_string(self):
        self.assertFalse(self.solution.wordPattern("", "dog cat"))
        self.assertFalse(self.solution.wordPattern("a", ""))

    def test_single_character_pattern(self):
        self.assertTrue(self.solution.wordPattern("a", "dog"))
        self.assertFalse(self.solution.wordPattern("a", "dog cat"))

if __name__ == "__main__":
    unittest.main(exit=False)
    print("All Test Cases Passed!")
