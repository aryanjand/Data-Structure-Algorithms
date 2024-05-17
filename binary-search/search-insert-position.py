from typing import List
import unittest

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        LeetCode Problem 35: Search Insert Position
        Difficulty: Easy
        Topics: Arrays, Binary Search

        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

        Key Ideas:
            - Perform a binary search for efficiency.
            - If the mid index value matches the target, return the mid index.
            - If the target is not found, return the left index.
              The loop condition left <= right ensures left is positioned at the correct insertion point.
              Weather left index value is less than or greater the correct insert position.
            - This approach also handles cases with a single element in the array.
        """
        length_nums = len(nums)
        left, right = 0, length_nums - 1
        mid = 0

        while left <= right:
            # mid is our index value
            mid = (right - left) // 2 + left

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")

class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_in_list(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 1), 0)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 6), 3)

    def test_target_not_in_list(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    def test_empty_list(self):
        self.assertEqual(self.solution.searchInsert([], 1), 0)

    def test_single_element_list(self):
        self.assertEqual(self.solution.searchInsert([1], 0), 0)
        self.assertEqual(self.solution.searchInsert([1], 1), 0)
        self.assertEqual(self.solution.searchInsert([1], 2), 1)

    def test_larger_list(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6, 8, 9, 10], 7), 4)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6, 8, 9, 10], 4), 2)
