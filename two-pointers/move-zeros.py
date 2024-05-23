from typing import List
import unittest

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        LeetCode Problem 283: Move Zeroes
        Difficulty: Easy
        Topics: Arrays, Two Pointers

        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        Key Ideas:
        - Use two pointers to iterate through the array: one to track the current position and one to find non-zero elements.
        - Swap all the non-zero elements with zero's to the front of the array, maintaining their relative order.
        - This will move all the zero's to the back and non-zero to the front-of-the-array while maintain order.

        Args:
        nums (List[int]): The input list of integers to be modified in-place.

        Returns:
        None: The function modifies the input list in-place and does not return a value.
        """

        left = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_moveZeroes(self):
        # Test case 1: Mixed zeros and non-zeros
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

        # Test case 2: All zeros
        nums = [0, 0, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0, 0])

        # Test case 3: No zeros
        nums = [1, 2, 3, 4, 5]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

        # Test case 4: Zeros at the beginning
        nums = [0, 0, 1, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

        # Test case 5: Zeros at the end
        nums = [1, 2, 3, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

        # Test case 6: Single element (zero)
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

        # Test case 7: Single element (non-zero)
        nums = [1]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
