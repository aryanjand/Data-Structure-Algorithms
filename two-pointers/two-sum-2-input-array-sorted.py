from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]

            if target > sum:
                left += 1
            elif target < sum:
                right -= 1
            else:
                return [left + 1, right + 1] # Indices start at 1
        return [-1, -1] # Default return if no solution


sol = Solution()

# Normal test cases
print(sol.twoSum([2, 7, 11, 15], 9) == [1, 2]) # Output: True
print(sol.twoSum([3, 2, 4], 6) == [2, 3]) # Output: False
print(sol.twoSum([3, 3], 6) == [1, 2]) # Output: True
print(sol.twoSum([-1, 0], -1) == [1, 2]) # Output: True
print(sol.twoSum([-3, 4, 3, 90], 0) == [1, 3]) # Output: True
print(sol.twoSum([0, 0, 3, 4], 0) == [1, 2]) # Output: True
print("All test cases passed!")
