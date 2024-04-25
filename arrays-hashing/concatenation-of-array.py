from typing import List

class Solution:
    def getConcatenation_solution_1(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        return nums + nums

    def getConcatenation_solution_2(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(2n) -> O(n)
        len_nums = len(nums)
        for i in range(len_nums):
            nums.append(nums[i])
        return nums

def test_getConcatenation():
    solution = Solution()
    # Test with an empty list
    assert solution.getConcatenation_solution_1([]) == []
    assert solution.getConcatenation_solution_2([]) == []

    # Test with a single element
    assert solution.getConcatenation_solution_1([1]) == [1, 1]
    assert solution.getConcatenation_solution_2([1]) == [1, 1]

    # Test with multiple elements
    assert solution.getConcatenation_solution_1([1, 2, 3]) == [1, 2, 3, 1, 2, 3]
    assert solution.getConcatenation_solution_2([1, 2, 3]) == [1, 2, 3, 1, 2, 3]

    # Test with a large list
    nums = [i for i in range(10**6)]
    assert solution.getConcatenation_solution_1(nums) == nums + nums
    assert solution.getConcatenation_solution_2(nums[:]) == nums + nums

test_getConcatenation()
print("All Test Cases Passed!")
