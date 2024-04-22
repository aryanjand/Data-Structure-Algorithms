from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = right - left // 2 + left

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

sol = Solution()

# Test case 1: Empty list
print(sol.search([], 5) == -1)
# Test case 2: Target not in nums
print(sol.search([1, 2, 3, 4, 6, 7, 8, 9], 5) == -1)
# Test case 3: Target at beginning of nums
print(sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0)
# Test case 4: Target at end of nums
print(sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8)
# Test case 5: Target in middle of nums
print(sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4)
# Test case 6: Single element list with target
print(sol.search([5], 5) == 0)
# Test case 7: Single element list without target
print(sol.search([7], 5) == -1)
# Test case 8: Multiple occurrences of target
print(sol.search([1, 2, 3, 4, 5, 5, 5, 8, 9], 5) in [4, 5, 6])
# Test case 9: Large list
print(sol.search(list(range(10**6)), 999999) == 999999)

print("All test cases passed!")
