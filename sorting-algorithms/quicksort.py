from typing import List
from random import randint
import time

class Solution:
    def partition_1(self, nums: List[int], start_index: int, end_index: int) -> int:
        pivot_vaule = nums[end_index]
        partition_index = start_index

        for i in range(start_index, end_index):
            if nums[i] <= pivot_vaule:
                nums[i], nums[partition_index] = nums[partition_index], nums[i]
                partition_index += 1
        nums[partition_index], nums[end_index] = nums[end_index], nums[partition_index]
        return partition_index

    def partition_2(self, nums: List[int], start_index: int, end_index: int) -> int:
        pivot_index = randint(start_index, end_index)
        pivot_value = nums[pivot_index]

        # swap the pivot element to the end_index
        nums[pivot_index], nums[end_index] = nums[end_index], nums[pivot_index]

        # Partition the subarray around the pivot
        partition_index = start_index  # Index of the smaller element
        for current_index in range(start_index, end_index):
            if nums[current_index] <= pivot_value:
                nums[current_index], nums[partition_index] = nums[partition_index], nums[current_index]
                partition_index += 1

        # swap the pivot element to its final position
        nums[partition_index], nums[end_index] = nums[end_index], nums[partition_index]

        return partition_index

    def quicksort(self, nums: List[int]) -> List[int]:
        """
        Time:
            Worst Case: O(N^2)
            Avgrage Case: O(N log N)
        Space: O(log N)
        Stable: No
        Method: Partitioning

        Quicksort is a divide-and-conquer algorithm that divides the input list into two partitions,
        recursively sorts the partitions, and then combines the sorted partitions.
        This process continues until the entire list is sorted.
        """
        length = len(nums)
        def sort(nums: List[int], start_index: int, end_index: int):
            # check if indexes are valid
            if start_index < end_index:
                # partition_index = self.partition_1(nums, start_index, end_index)
                partition_index = self.partition_2(nums, start_index, end_index)
                sort(nums, start_index, partition_index - 1)
                sort(nums, partition_index + 1, end_index)
        sort(nums, 0, length - 1)
        return nums


def test_sort():
    solution = Solution()

    # Create a large array
    large_array = [i for i in range(10**4, 0, -1)]
    large_array_sorted = sorted(large_array)

    # Create a super large array
    super_large_array = [i for i in range(10**5, 0, -1)]
    super_large_array_sorted = sorted(super_large_array)

    # Create a super large array
    super_super_large_array = [i for i in range(10**6, 0, -1)]
    super_super_large_array_sorted = sorted(super_super_large_array)

    n_squared_array = [i for i in range(10**6, 0, -1)]
    n_squared_array_sorted = sorted(n_squared_array)

    # Test quicksort
    assert solution.quicksort([]) == []
    assert solution.quicksort([3, 5, 3, 6, 5, 7, 7, 6, 8]) == [3, 3, 5, 5, 6, 6, 7, 7, 8]
    assert solution.quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    # Test large array
    start_time = time.time()
    sorted_array_1 = solution.quicksort(large_array.copy())
    end_time = time.time()
    print(f"Quicksort took {end_time - start_time:.2f} seconds to sort the large array!")

    # Test super large array
    start_time = time.time()
    sorted_array_2 = solution.quicksort(super_large_array.copy())
    end_time = time.time()
    print(f"Quicksort took {end_time - start_time:.2f} seconds to sort the super large array!")


    # Test super super large array
    start_time = time.time()
    sorted_array_3 = solution.quicksort(super_super_large_array.copy())
    end_time = time.time()
    print(f"Quicksort took {end_time - start_time:.2f} seconds to sort the SUPER SUPER LARGE ARRAY!")


    # Test super super large array
    start_time = time.time()
    sorted_array_4 = solution.quicksort(n_squared_array.copy())
    end_time = time.time()
    print(f"Quicksort took {end_time - start_time:.2f} seconds to sort the Reversed Sorted Array!")


    assert sorted_array_1 == large_array_sorted
    assert sorted_array_2 == super_large_array_sorted
    assert sorted_array_3 == super_super_large_array_sorted
    assert sorted_array_4 == n_squared_array_sorted

test_sort()
print("All Test Cases Passed!")
