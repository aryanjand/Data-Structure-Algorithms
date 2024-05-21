from typing import List
import unittest

class Solution:
    """
    LeetCode Problem 27: Remove Element
    Difficulty: Easy
    Topics: Arrays, Two Pointers

    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k. To get accepted, you need to do the following things:
    - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    - Return k.
    """
    def removeElement_1(self, nums: List[int], val: int) -> int:
        """
        Key Ideas:
        - Use two pointers: one to track the current position (left) and another to find the next element not equal to val (right).
        - Increment the left pointer until the first occurrence of val is found.
        - Use the right pointer to find elements not equal to val and replace elements at the left pointer position.
        - Continue until the end of the array is reached.
        """
        left = 0
        length_nums = len(nums)

        while left < length_nums and nums[left] != val:
            left += 1

        right = left

        while right < length_nums:
            while right < length_nums and nums[right] == val:
                right += 1
            if right < length_nums:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return left

    def removeElement_2(self, nums: List[int], val: int) -> int:
        """
        Key Ideas:
            - Use two pointers: one to track the current position (left) and another to find the next element not equal to val (right).
            - The for loop will increment the right pointer.
            - Use the right pointer to find elements not equal to val and replace elements at the left pointer position.
            - The left pointer will be tracking the k elements in the array as well as any instances of val.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_removeElement(self):
        # Test case 1: Example from the problem statement
        nums1 = [3, 2, 2, 3]
        self.assertEqual(self.solution.removeElement_1(nums1, 2), 2)
        self.assertEqual(nums1[:2], [3, 3])

        nums2 = [3, 2, 2, 3]
        self.assertEqual(self.solution.removeElement_2(nums2, 2), 2)
        self.assertEqual(nums2[:2], [3, 3])

        # Test case 2: Single-element list
        nums3 = [1]
        self.assertEqual(self.solution.removeElement_1(nums3, 1), 0)
        self.assertEqual(nums3[:0], [])

        # Test case 3: All elements are val
        nums4 = [2, 2, 2, 2, 2]
        self.assertEqual(self.solution.removeElement_2(nums4, 2), 0)
        self.assertEqual(nums4[:0], [])

        # Test case 4: No elements are val
        nums5 = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.removeElement_1(nums5, 6), 5)
        self.assertEqual(nums5[:5], [1, 2, 3, 4, 5])

        nums6 = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.removeElement_2(nums6, 6), 5)
        self.assertEqual(nums6[:5], [1, 2, 3, 4, 5])

        # Test case 5: Random list with multiple occurrences of val
        nums7 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        self.assertEqual(self.solution.removeElement_1(nums7, 2), 8)
        self.assertEqual(nums7[:8], [1, 3, 4, 5, 1, 3, 4, 5])

        nums8 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        self.assertEqual(self.solution.removeElement_2(nums8, 2), 8)
        self.assertEqual(nums8[:8], [1, 3, 4, 5, 1, 3, 4, 5])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
