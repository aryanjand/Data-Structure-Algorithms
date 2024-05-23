from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.
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
