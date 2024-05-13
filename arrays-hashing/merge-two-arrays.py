from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays nums1 and nums2 into nums1. Do not return anything, modify nums1 in-place instead.

        Approach:
        Start from the end of both arrays since nums1 has enough space to hold all elements.
        Compare elements from nums1 and nums2, and place the larger element at the end of nums1.

        Steps:
        1. Initialize 'last' pointer to m + n - 1, 'm_index' to m - 1, and 'n_index' to n - 1.
        2. While both m and n are greater than 0, compare nums1[m_index] and nums2[n_index].
            - If nums1[m_index] is greater, place it at nums1[last] and decrement m and m_index.
            - If nums2[n_index] is greater, place it at nums1[last] and decrement n and n_index.
            - Decrement last.
        3. If there are remaining elements in nums2, place them in nums1 starting from the beginning.

        Time complexity: O(m + n)
        Space complexity: O(1)
        """
        last = m + n - 1
        m_index, n_index = m - 1, n - 1

        while m > 0 and n > 0:
            if nums1[m_index] > nums2[n_index]:
                nums1[last] = nums1[m_index]
                m, m_index = m - 1, m_index - 1
            else:
                nums1[last] = nums2[n_index]
                n, n_index = n - 1, n_index - 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n_index]
            n, n_index = n - 1, n_index - 1
            last -= 1


def test_merge():
    solution = Solution()
    # Test with nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    # Test with nums1 = [1], m = 1, nums2 = [], n = 0
    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    assert nums1 == [1]

    # Test with nums1 = [0], m = 0, nums2 = [1], n = 1
    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    # Test with nums1 = [4, 5, 6, 0, 0, 0], m = 3, nums2 = [1, 2, 3], n = 3
    nums1 = [4, 5, 6, 0, 0, 0]
    solution.merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]

test_merge()
print("All Test Cases Passed!")
