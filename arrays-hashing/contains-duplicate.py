from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists = set()

        for i in range(len(nums)):
            if nums[i] in exists:
                return True
            exists.add(nums[i])

        return False

def test_contains_duplicate():
    solution = Solution()

    # Test case with duplicates
    nums1 = [1, 2, 3, 1]
    assert solution.containsDuplicate(nums1) == True

    # Test case without duplicates
    nums2 = [1, 2, 3, 4]
    assert solution.containsDuplicate(nums2) == False

    # Test case with empty list
    nums3 = []
    assert solution.containsDuplicate(nums3) == False

    # Test case with large list containing duplicates
    nums4 = [1, 2, 3] * 1000
    assert solution.containsDuplicate(nums4) == True

    # Test case with large list without duplicates
    nums5 = list(range(1000))
    assert solution.containsDuplicate(nums5) == False

# Run the test cases
test_contains_duplicate()
print("All test cases passed!")
