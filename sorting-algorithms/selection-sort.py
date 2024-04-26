from typing import List
import time

class Solution:
    def selection_sort_1(self, nums: List[int]) -> List[int]:
        """
        Time: O(N^2)
        Space: O(N)
        Stable: No
        Method: Selection

        The algorithm starts with an empty sorted list on the left and the unsorted list on the right.
        It then iterates through the unsorted list, selecting the smallest (or largest)
        element and moving it to the end of the sorted list.
        This process continues until all elements are sorted.
        """
        sorted_nums = []
        len_nums = len(nums)
        for _ in range(len_nums):
            min_val = float('inf')
            min_idx = -1
            for idx, num in enumerate(nums):
                if num < min_val:
                    min_val = num
                    min_idx = idx
            sorted_nums.append(min_val)
            nums[min_idx] = float('inf') # Mark the selected element as infinity
        return sorted_nums



    def selection_sort_2(self, nums: List[int]) -> List[int]:
        """
        Time: O(N)
        Space: O(1)
        Stable: No
        Method: Selection

        This variation of selection sort improves space complexity by performing the sorting in-place.
        It iterates through the list, selecting the minimum element from the unsorted portion and swapping it with the first unsorted element.
        The process continues until all elements are sorted.
        """
        len_nums = len(nums)
        for i in range(len_nums - 1): # We need to do n-2 passes
        # elements from i till n-1 are candidates
            min_index = i
            for j in range(i + 1, len_nums): # Check the unsorted portion of the list
                if (nums[j] < nums[min_index]): # find the index of the minimum element
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums


def test_sort():
    solution = Solution()

    # Create a large array
    large_array = [i for i in range(10**5, 0, -1)]
    large_array_sorted = sorted(large_array)

    # Test selection_sort_1
    assert solution.selection_sort_1([]) == []
    assert solution.selection_sort_1([3, 5, 3, 6, 5, 7, 7, 6, 8]) == [3, 3, 5, 5, 6, 6, 7, 7, 8]
    assert solution.selection_sort_1([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    start_time = time.time()
    sorted_array_1 = solution.selection_sort_1(large_array.copy())
    end_time = time.time()
    print(f"Selection Sort 1 took {end_time - start_time:.2f} seconds to sort the large array")
    assert sorted_array_1 == large_array_sorted

    # Test selection_sort_2
    assert solution.selection_sort_2([]) == []
    assert solution.selection_sort_2([3, 5, 3, 6, 5, 7, 7, 6, 8]) == [3, 3, 5, 5, 6, 6, 7, 7, 8]
    assert solution.selection_sort_2([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    start_time = time.time()
    sorted_array_2 = solution.selection_sort_2(large_array.copy())
    end_time = time.time()
    print(f"Selection Sort 2 took {end_time - start_time:.2f} seconds to sort the large array")
    assert sorted_array_2 == large_array_sorted



test_sort()
print("All Test Cases Passed!")
