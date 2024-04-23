from collections import defaultdict

class Solution:
    def isAnagram_unicode(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s, map_t = defaultdict(int), defaultdict(int)

        for index in range(len(s)):
            map_s[s[index]] += 1
            map_t[t[index]] += 1

        return map_s == map_t

    # In order for the array solution
    # to haddle unicode we need close 150,000 slots
    def isAnagram_lowercase(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        array_s, array_t = [0] * 26, [0] * 26

        for index in range(len(s)):
            array_s[ord(s[index]) - ord("a")] += 1
            array_t[ord(t[index]) - ord("a")] += 1

        return array_s == array_t
def test_isAnagram_lowercase():
    solution = Solution()
    assert solution.isAnagram_lowercase("", "") == True
    assert solution.isAnagram_lowercase("anagram", "nagaram") == True
    assert solution.isAnagram_lowercase("rat", "car") == False
    assert solution.isAnagram_lowercase("listen", "silent") == True
    assert solution.isAnagram_lowercase("hello", "world") == False
    assert solution.isAnagram_lowercase("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba") == True

def test_isAnagram_unicode():
    solution = Solution()
    assert solution.isAnagram_unicode("", "") == True
    assert solution.isAnagram_unicode("anagram", "nagaram") == True
    assert solution.isAnagram_unicode("rat", "car") == False
    assert solution.isAnagram_unicode("listen", "silent") == True
    assert solution.isAnagram_unicode("hello", "world") == False
    assert solution.isAnagram_unicode("abcde12345", "54321edcba") == True

test_isAnagram_lowercase()
test_isAnagram_unicode()

print("All Test Cases Passed!")
