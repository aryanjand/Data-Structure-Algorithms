from typing import List
import time

class Solution:
    def insertion_sort(self, nums: List[int]) -> List[int]:
        """
        Time: O(N^2)
        Space: O(1)
        Stable: Yes
        Method: Insertion

        Insertion sort builds the final sorted list one item at a time.
        It takes each element from the input list and inserts it into its correct position in the sorted list.
        """
        length = len(nums)
        for current_index in range(1, length):
            current_value = nums[current_index]
            shift_index = current_index
            # Find the correct position to insert the current value in the sorted subarray
            while shift_index > 0 and nums[shift_index - 1] > current_value:
                nums[shift_index] = nums[shift_index - 1]
                shift_index -= 1
            # Insert the current value in its correct position
            nums[shift_index] = current_value
        return nums

def test_sort():
    solution = Solution()

    # Create a large array
    large_array = [i for i in range(10**4, 0, -1)]
    large_array_sorted = sorted(large_array)

    # Test insertion sort
    assert solution.insertion_sort([]) == []
    assert solution.insertion_sort([3, 5, 3, 6, 5, 7, 7, 6, 8]) == [3, 3, 5, 5, 6, 6, 7, 7, 8]
    assert solution.insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    start_time = time.time()
    sorted_array_1 = solution.insertion_sort(large_array.copy())
    end_time = time.time()
    print(f"Insertion Sort took {end_time - start_time:.2f} seconds to sort the large array")
    assert sorted_array_1 == large_array_sorted

test_sort()
print("All Test Cases Passed!")
