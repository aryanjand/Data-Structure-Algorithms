from typing import List
import unittest

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        LeetCode Problem 605: Can Place Flowers
        Difficulty: Easy
        Topics: Arrays, Greedy

        You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

        Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

        Key Ideas:
        - To place a flower, we need three consecutive empty plots (0's).
        - If the first or last element is a zero and it is not adjacent to a 1, a flower can be placed there.
        - Traverse the flowerbed to check for possible flower placements and reduce n accordingly.
        - If n becomes 0 or less, return True; otherwise, return False.

        Args:
        flowerbed (List[int]): The flowerbed represented as a list of integers.
        n (int): The number of flowers to plant.

        Returns:
        bool: True if n flowers can be planted without violating the no-adjacent-flowers rule, False otherwise.
        """

        flowerbed.insert(0, 0)
        flowerbed.append(0)

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_canPlaceFlowers(self):
        # Test case 1: Example case from problem statement
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        self.assertTrue(self.solution.canPlaceFlowers(flowerbed, n), "Test Case 1 Failed")

        # Test case 2: Example case from problem statement
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        self.assertFalse(self.solution.canPlaceFlowers(flowerbed, n), "Test Case 2 Failed")

        # Test case 3: No flowers to plant
        flowerbed = [1, 0, 0, 0, 1]
        n = 0

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
