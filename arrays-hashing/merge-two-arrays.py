class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        This problem involves starting from the last element of nums1 and nums2 and comparing them,
        placing the larger of the two at the end of nums1, and then moving the indices backwards.
        This is repeated until all elements from nums2 are merged into nums1.
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
