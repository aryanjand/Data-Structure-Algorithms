from typing import List
import unittest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        LeetCode Problem 26: Remove Duplicates from Sorted Array
        Difficulty: Easy
        Topics: Arrays, Two Pointers

        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
        The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
        - Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
          The remaining elements of nums are not important as well as the size of nums.
        - Return k.

        Key Ideas:
            - Both pointers can start at index 1, because we know the first element is unique.
            - We can determine if an element is a duplicate or unique by comparing it with the previous index.
            - There is no need to swap elements because we only care about the first k elements.
        """
        if not nums:
            return 0

        length_nums = len(nums)
        left, right = 1, 1

        while right < length_nums:
            if nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeDuplicates(self):
        nums1 = [1, 1, 2]
        self.assertEqual(self.solution.removeDuplicates(nums1), 2)
        self.assertEqual(nums1[:2], [1, 2])

        nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(self.solution.removeDuplicates(nums2), 5)
        self.assertEqual(nums2[:5], [0, 1, 2, 3, 4])

        nums3 = []
        self.assertEqual(self.solution.removeDuplicates(nums3), 0)
        self.assertEqual(nums3, [])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
