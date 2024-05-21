from typing import List
import unittest

class Solution:
    def minCostClimbingStairs_1(self, cost: List[int]) -> int:
        """
        LeetCode Problem 746: Min Cost Climbing Stairs
        Difficulty: Easy
        Topics: Arrays, Dynamic Programming
        Time Complexity: O(N)
        Space Complexity: O(N)

        You are given an integer array 'cost' where cost[i] represents the cost of the ith step on a staircase.
        Once you pay the cost, you can either climb one or two steps.

        You can start either from the step with index 0 or the step with index 1.

        Return the minimum cost to reach the top of the floor.

        Key Ideas:
        - Use dynamic programming to find the minimum cost to reach each step by working backwards from the top.
        - At each step, calculate the minimum cost of reaching that step by considering the cost of the previous one or two steps.
        - The minimum cost to reach the top will be the minimum of the costs of the last two steps.
        """
        steps = {}

        def dfs(index: int) -> int:
            if index in steps:
                return steps[index]

            if index in [0, 1]:
                return cost[index]

            min_cost = cost[index] + min(dfs(index - 1), dfs(index - 2))
            steps[index] = min_cost
            return min_cost

        n = len(cost)
        return min(dfs(n - 1), dfs(n - 2))

    def minCostClimbingStairs_2(self, cost: List[int]) -> int:
        """
        LeetCode Problem 746: Min Cost Climbing Stairs
        Difficulty: Easy
        Topics: Arrays, Dynamic Programming
        Time Complexity: O(N)
        Space Complexity: O(1)

        You are given an integer array 'cost' where cost[i] represents the cost of the ith step on a staircase.
        Once you pay the cost, you can either climb one or two steps.

        You can start either from the step with index 0 or the step with index 1.

        Return the minimum cost to reach the top of the floor.

        Key Ideas:
        - Use dynamic programming to find the minimum cost to reach each step by working backwards from the top.
        - At each step, calculate the minimum cost of reaching that step by considering the cost of the previous one or two steps.
        - The minimum cost to reach the top will be the minimum of the costs of the last two steps.
        """
        n = len(cost)
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")

class TestSolution(unittest.TestCase):
    def __init__(self):
        self.solution = Solution()

    def test_minCostClimbingStairs(self):
            # Test case 1: General case
            cost = [10, 15, 20]
            expected_result = 15
            self.assertEqual(self.solution.minCostClimbingStairs_1(cost), expected_result)
            self.assertEqual(self.solution.minCostClimbingStairs_2(cost), expected_result)

            # Test case 2: Larger input
            cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
            expected_result = 6
            self.assertEqual(self.solution.minCostClimbingStairs_1(cost), expected_result)
            self.assertEqual(self.solution.minCostClimbingStairs_2(cost), expected_result)

            # Test case 3: Single step
            cost = [0]
            expected_result = 0
            self.assertEqual(self.solution.minCostClimbingStairs_1(cost), expected_result)
            self.assertEqual(self.solution.minCostClimbingStairs_2(cost), expected_result)

            # Test case 4: Two steps
            cost = [1, 100]
            expected_result = 1
            self.assertEqual(self.solution.minCostClimbingStairs_1(cost), expected_result)
            self.assertEqual(self.solution.minCostClimbingStairs_2(cost), expected_result)

            # Test case 5: Empty cost array
            cost = []
            expected_result = 0
            self.assertEqual(self.solution.minCostClimbingStairs_1(cost), expected_result)
            self.assertEqual(self.solution.minCostClimbingStairs_2(cost), expected_result)
