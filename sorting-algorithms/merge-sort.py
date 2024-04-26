from typing import List
import time

class Solution:

    def merge(self, left_array: List[int], right_array: List[int], result_nums_array: List[int]) -> List[int]:

        len_left_array, len_right_array, len_result_array = len(left_array), len(right_array), len(result_nums_array)
        left_index = right_index = insert_index = 0

        while left_index < len_left_array and right_index < len_right_array:
            if left_array[left_index] <= right_array[right_index]:
                result_nums_array[insert_index] = left_array[left_index]
                left_index += 1
            else:
                result_nums_array[insert_index] = right_array[right_index]
                right_index += 1
            insert_index += 1

        while left_index < len_left_array:
            result_nums_array[insert_index] = left_array[left_index]
            left_index += 1
            insert_index += 1

        while right_index < len_right_array:
            result_nums_array[insert_index] = right_array[right_index]
            right_index += 1
            insert_index += 1
        return result_nums_array


    def merge_sort(self, nums: List[int]) -> List[int]:
        """
        Time: O(N log(N))
        Space: O(N)
        Stable: Yes
        Method: Merging

        Merge sort is a divide-and-conquer algorithm that divides the input list into two halves,
        recursively sorts the halves, and then merges the sorted halves.
        This process continues until the entire list is sorted.
        """

        length = len(nums)
        if length < 2:
            return nums
        left_array = nums[:length // 2]
        right_array = nums[length // 2:]

        sorted_left_array = self.merge_sort(left_array)
        sorted_right_array = self.merge_sort(right_array)
        return self.merge(sorted_left_array, sorted_right_array, nums)


def test_sort():
    solution = Solution()

    # Create a large array
    large_array = [i for i in range(10**4, 0, -1)]
    large_array_sorted = sorted(large_array)

    # Create a super large array
    super_large_array = [i for i in range(10**5, 0, -1)]
    super_large_array_sorted = sorted(super_large_array)

    # Test merge sort
    assert solution.merge_sort([]) == []
    assert solution.merge_sort([3, 5, 3, 6, 5, 7, 7, 6, 8]) == [3, 3, 5, 5, 6, 6, 7, 7, 8]
    assert solution.merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    start_time = time.time()
    sorted_array_1 = solution.merge_sort(large_array.copy())
    end_time = time.time()
    print(f"Merge Sort took {end_time - start_time:.2f} seconds to sort the large array")

    start_time = time.time()
    sorted_array_2 = solution.merge_sort(super_large_array.copy())
    end_time = time.time()
    print(f"Merge Sort took {end_time - start_time:.2f} seconds to sort the super large array")

    assert sorted_array_1 == large_array_sorted
    assert sorted_array_2 == super_large_array_sorted

test_sort()
print("All Test Cases Passed!")
