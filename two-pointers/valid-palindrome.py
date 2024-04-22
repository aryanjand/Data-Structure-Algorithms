class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            while left < right and not s[left].isalnum():
                # It's not <= because when there are only special characters,
                # we want the indexes to equal one another
                # and then stop so that it can return True
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True



sol = Solution()

# Test the isPalindrome method
print(sol.isPalindrome("A man, a plan, a canal: Panama!"))  # Output: True
print(sol.isPalindrome("race a car"))  # Output: False
print(sol.isPalindrome("RAce    Car")) # Output: True
print(sol.isPalindrome(".[;.[;,;.][;;';.';.")) # Output: True
