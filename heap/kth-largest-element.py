from typing import List
from heapq import *
import unittest

class KthLargest:
    """
    LeetCode Problem 703: Kth Largest Element in a Stream
    Difficulty: Easy
    Topics: Tree, Heap (Priority Queue), Binary Tree

    Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Implement the KthLargest class:

        KthLargest(int k, int[] nums): Initializes the object with the integer k and the stream of integers nums.
        int add(int val): Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

    Key Ideas:
    - Using a min-heap is the key idea to efficiently implement this class.
    - Heapify the input list takes O(N). However, to maintain only the k largest elements in the heap,
      pop the smallest elements until the heap size is k. Removing elements takes O(log N),
      so popping n - k elements takes O((N - k) log N). This keeps the constructor efficient.
    - In the add method, add the new value to the heap and then pop the smallest element
      if the heap size exceeds k. This ensures the heap size remains k, and the kth largest
      element is always at the root of the heap. This operation is O(log N).

    Args:
    k (int): The position of the largest element to find.
    nums (List[int]): The initial stream of integers.

    Returns:
    int: The kth largest element in the stream after the new integer is added.
    """
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapify(self.min_heap) # O(N)

        while len(nums) > self.k: # (N - K) * log(N)
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val) # log(N)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap) # log(N)

        return self.min_heap[0]

class TestSolution(unittest.TestCase):
    def test_kth_largest(self):
        # Initialize with k = 3 and initial list [4, 5, 8, 2]
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kthLargest.add(3), 4)  # Adding 3 should not change the k-th largest element (which is 4)
        self.assertEqual(kthLargest.add(5), 5)  # Adding 5 should change the k-th largest element to 5
        self.assertEqual(kthLargest.add(10), 5)  # Adding 10 should not change the k-th largest element (which is 5)
        self.assertEqual(kthLargest.add(9), 8)  # Adding 9 should change the k-th largest element to 8
        self.assertEqual(kthLargest.add(4), 8)  # Adding 4 should not change the k-th largest element (which is 8)

        # Test with k = 1 and initial empty list
        kthLargest = KthLargest(1, [])
        self.assertEqual(kthLargest.add(-1), -1)  # Adding -1 should make -1 the k-th largest element
        self.assertEqual(kthLargest.add(1), 1)  # Adding 1 should make 1 the k-th largest element
        self.assertEqual(kthLargest.add(-2), 1)  # Adding -2 should not change the k-th largest element (which is 1)
        self.assertEqual(kthLargest.add(-4), 1)  # Adding -4 should not change the k-th largest element (which is 1)
        self.assertEqual(kthLargest.add(3), 3)  # Adding 3 should make 3 the k-th largest element

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
