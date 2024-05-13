from typing import List

class Solution:
    def replaceElements(self, array: List[int]) -> List[int]:
        """
        Problem:
            Given an array, replace every element in that array with the greatest element
            among the elements to its right, and replace the last element with -1.
        """
        # reverse the array
        array = array[::-1] # O(N)
        # We know initail max is -1
        current_max = -1
        length = len(array)

        for i in range(length): # O(N)
           potential_new_max = array[i]
           array[i] = current_max
           current_max = max(current_max, potential_new_max)

        return array[::-1] # O(N)

def test_replaceElements():
    solution = Solution()

    # Test with an empty list
    assert solution.replaceElements([]) == []

    # Test with a single-element list
    assert solution.replaceElements([5]) == [-1]

    # Test with a list of positive integers
    assert solution.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]

    # Test with a list of negative integers
    assert solution.replaceElements([-5, -2, -10, -3, -1]) == [-1, -1, -1, -1, -1]

    # Test with a list of mixed positive and negative integers
    assert solution.replaceElements([-5, 2, -10, 3, -1]) == [3, 3, 3, -1, -1]

    # Test with a large list
    assert solution.replaceElements(list(range(1000000))) == [999999] * 999999 + [-1]

    print("All Test Cases Passed!")

test_replaceElements()
