from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index in range(len(nums)):
            if target - nums[index] in map:
                return [index, map[target - nums[index]]]
            map[nums[index]] = index

        return [-1,-1]

def test_twoSum():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert solution.twoSum([0, 4, 3, 0], 0) == [0, 3]

    assert solution.twoSum_hashmap([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum_hashmap([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum_hashmap([3, 3], 6) == [0, 1]
    assert solution.twoSum_hashmap([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert solution.twoSum_hashmap([0, 4, 3, 0], 0) == [0, 3]

test_twoSum()
print("All Tests Passed!")
