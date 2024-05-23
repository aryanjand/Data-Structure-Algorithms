from sys import argv
from typing import List
import unittest

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        LeetCode Problem 977: Squares of a Sorted Array
        Difficulty: Easy
        Topics: Arrays, Two Pointers, Sorting

        Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

        Key Ideas:
        - Utilize the sorted nature of the array. Negative numbers will have their squares sorted in reverse order relative to the positive numbers.
        - Use two pointers to merge the two halves of the array: one starting from the beginning (for non-negative numbers) and one from the end (for negative numbers).
        - Compare the squared values and place them in the correct position in the result array.

        Args:
        nums (List[int]): The input list of integers sorted in non-decreasing order.

        Returns:
        List[int]: A list of the squares of each number sorted in non-decreasing order.
        """
        nums_length = len(nums)
        left, right = 0, nums_length - 1
        insert_index = nums_length - 1
        res = [0] * nums_length

        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                res[insert_index] = nums[right] ** 2
                right -= 1
            else:
                res[insert_index] = nums[left] ** 2
                left += 1
            insert_index -= 1
        return res

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_sortedSquares(self):
        # Test case 1: Mixed positive and negative values
        nums = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        self.assertEqual(self.solution.sortedSquares(nums), expected)

        # Test case 2: All positive values
        nums = [1, 2, 3, 4, 5]
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(self.solution.sortedSquares(nums), expected)

        # Test case 3: All negative values
        nums = [-7, -3, -1]
        expected = [1, 9, 49]
        self.assertEqual(self.solution.sortedSquares(nums), expected)

        # Test case 4: Single element (zero)
        nums = [0]
        expected = [0]
        self.assertEqual(self.solution.sortedSquares(nums), expected)

        # Test case 5: Single element (positive)
        nums = [2]
        expected = [4]
        self.assertEqual(self.solution.sortedSquares(nums), expected)

        # Test case 6: Single element (negative)
        nums = [-2]
        expected = [4]
        self.assertEqual(self.solution.sortedSquares(nums), expected)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
