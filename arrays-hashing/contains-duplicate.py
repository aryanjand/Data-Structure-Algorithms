from typing import List
import unittest

class Solution:
    """
    LeetCode Problem 217: Contains Duplicate
    Difficulty: Easy
    Topics: Arrays

    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """

    def containsDuplicate_1(self, nums: List[int]) -> bool:
        """
        Check if any value in the array appears at least twice using a hash set.

        Time Complexity: O(N)
        Space Complexity: O(N)

        Key Ideas:
        - Use a hash set (`exists`) to store unique elements encountered so far.
        - Iterate through the array and check if each element is already in the hash set.
        - If an element is already in the set, return True; otherwise, add it to the set and continue.
        - If the loop completes without finding any duplicates, return False.

        Args:
        nums (List[int]): The input integer array.

        Returns:
        bool: True if any value appears at least twice, False otherwise.
        """
        exists = set()

        for i in range(len(nums)):
            if nums[i] in exists:
                return True
            exists.add(nums[i])
        return False

    def containsDuplicate_2(self, nums: List[int]) -> bool:
        """
        Check if any value in the array appears at least twice by sorting the array.

        Time Complexity: O(N log(N))
        Space Complexity: O(1)

        Key Ideas:
        - Sort the input array, which groups equal elements together.
        - Iterate through the sorted array and check if the current element is equal to the previous one (except for the first element to avoid an index out of bounds error).
        - If a duplicate is found, return True; otherwise, return False after checking all elements.

        Args:
        nums (List[int]): The input integer array.

        Returns:
        bool: True if any value appears at least twice, False otherwise.
        """
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                return True
        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate(self):
        nums1 = [1, 2, 3, 1]
        self.assertTrue(self.solution.containsDuplicate_1(nums1))
        self.assertTrue(self.solution.containsDuplicate_2(nums1))

        nums2 = [1, 2, 3, 4]
        self.assertFalse(self.solution.containsDuplicate_1(nums2))
        self.assertFalse(self.solution.containsDuplicate_2(nums2))

        nums3 = []
        self.assertFalse(self.solution.containsDuplicate_1(nums3))
        self.assertFalse(self.solution.containsDuplicate_2(nums3))

        nums4 = [1, 2, 3] * 1000
        self.assertTrue(self.solution.containsDuplicate_1(nums4))
        self.assertTrue(self.solution.containsDuplicate_2(nums4))

        nums5 = list(range(1000))
        self.assertFalse(self.solution.containsDuplicate_1(nums5))
        self.assertFalse(self.solution.containsDuplicate_2(nums5))

if __name__ == '__main__':
    unittest.main(exit=False)
    print("All test cases passed!")
