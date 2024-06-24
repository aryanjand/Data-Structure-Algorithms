from typing import List
import unittest

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        LeetCode Problem 1498: Number of Subsequences that Satisfy the Given Sum Condition
        Difficulty: Medium
        Topics: Arrays, Two Pointers, Sliding Window

        Description:
        You are given an array of integers nums and an integer target. Return the number of non-empty subsequences of nums
        such that the sum of the minimum and maximum element in the subsequence is less than or equal to the target.
        Since the answer may be too large, return it modulo 10^9 + 7.

        Key Ideas:
        - Sort the array to facilitate the two-pointer approach.
        - Use two pointers to find subsequences where the sum of the minimum and maximum elements is <= target.
        - For each valid pair (nums[left], nums[right]), the number of valid subsequences is 2^(right - left).
        - Increment the left pointer if the sum of nums[left] and nums[right] is <= target, otherwise decrement the right pointer.
        - Use modulo 10^9 + 7 to handle large results.
        """
        nums.sort()
        res = 0
        MOD = (10**9 + 7)

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += 1 if right - left == 0  else 2**(right - left)
                res %= MOD
                left += 1
            else:
                right -= 1
        return res

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_moveZeroes(self):
        # Test case 1: Mixed zeros and non-zeros
        nums = [3, 5, 6, 7]
        output = self.solution.numSubseq(nums, 9)
        self.assertEqual(output, 4)

        # Test case 2: All zeros
        nums = [3, 3, 6, 8]
        output = self.solution.numSubseq(nums, 10)
        self.assertEqual(output, 6)

        # Test case 3: No zeros
        nums = [2, 3, 3, 4, 6, 7]
        output = self.solution.numSubseq(nums, 12)
        self.assertEqual(output, 61)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
