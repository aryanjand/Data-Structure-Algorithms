from typing import List
import time

class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        """
        Time: O(N^2)
        Space: O(1)
        Stable: Yes
        Method: Exchanging

        Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
        The pass through the list is repeated until the list is sorted.
        """
        len_nums = len(nums)
        for k in range(len_nums):
            is_sorted = True
            for i in range(len_nums - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i] # Swap the elements
                    is_sorted = False
            if is_sorted:
                break
        return nums


def test_sort():
    solution = Solution()

    # Create a large array
    large_array = [i for i in range(10**4, 0, -1)]
    large_array_sorted = sorted(large_array)

    # Test bubble
    assert solution.bubble_sort([]) == []
    assert solution.bubble_sort([3, 5, 3, 6, 5, 7, 7, 6, 8]) == [3, 3, 5, 5, 6, 6, 7, 7, 8]
    assert solution.bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    start_time = time.time()
    sorted_array_1 = solution.bubble_sort(large_array.copy())
    end_time = time.time()
    print(f"Bubble Sort took {end_time - start_time:.2f} seconds to sort the large array")
    assert sorted_array_1 == large_array_sorted

test_sort()
print("All Test Cases Passed!")
