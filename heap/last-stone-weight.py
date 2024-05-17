from typing import List
import heapq
import unittest

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        LeetCode Problem 1046: Last Stone Weight
        Difficulty: Easy
        Topics: Arrays, Heap (Priority Queue)

        Given an array stones where stones[i] is the weight of the ith stone,
        play a game where you smash the heaviest two stones each turn until there is at most one stone left.

        Return the weight of the last remaining stone, or 0 if there are no stones left.

        Key Ideas:
            - Use a max heap (implemented with negated values) to get the heaviest stones efficiently.
            - Simulate the smashing of stones until there is at most one stone left.
            - If a stone is left over after the loop, add it back to the heap (making it a log n operation) N times.
        """

        if not stones:
            return 0

        stones = [-stone for stone in stones]
        heapq.heapify(stones) # O(n)

        while len(stones) > 1: # O(n)
            max_stone_1, max_stone_2 = -heapq.heappop(stones), -heapq.heappop(stones)

            if max_stone_2 > max_stone_1:
                heapq.heappush(stones, -(max_stone_2 - max_stone_1)) # O(log n)
            else:
                heapq.heappush(stones, -(max_stone_1 - max_stone_2)) # O(log n)

        return 0 if not stones else -heapq.heappop(stones)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lastStoneWeight(self):
        self.assertEqual(self.solution.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(self.solution.lastStoneWeight([1, 3]), 2)
        self.assertEqual(self.solution.lastStoneWeight([1]), 1)
        self.assertEqual(self.solution.lastStoneWeight([]), 0)
        self.assertEqual(self.solution.lastStoneWeight([5, 5, 5, 5, 5]), 0)
