from collections import defaultdict

class Solution:
    def climbStairs_memoization(self, n: int) -> int:
        memoization = defaultdict(int)

        def dfs(steps: int) -> int:
            if steps in memoization:
                return memoization[steps]

            if steps < 0:
                return 0
            elif steps == 0:
                return 1
                # Calculate the distinct number of ways to climb `steps` stairs
                # by summing up the results of climbing `steps-1` and `steps-2` stairs.
            memoization[steps] = dfs(steps - 1) + dfs(steps - 2)
            return memoization[steps]

        return dfs(n)

    def climbStairs_bottom_up(self, n: int) -> int:
        step1, step2 = 1, 1

        for i in range(1, n):
            # This loop runs n times, index value is 0 to n - 1.
            # Because we start with 1 step already taken (step1 = 1),
            # and we iterate to compute the remaining n - 1 steps or from range(1, n) needed to reach the nth step.
            step1, step2 = step2, step2 + step1

        return step2



def test_climbStairs():
    solution = Solution()
    # Test with n = 2
    assert solution.climbStairs_memoization(2) == 2
    assert solution.climbStairs_bottom_up(2) == 2

    # Test with n = 3
    assert solution.climbStairs_memoization(3) == 3
    assert solution.climbStairs_bottom_up(3) == 3

    # Test with n = 4
    assert solution.climbStairs_memoization(4) == 5
    assert solution.climbStairs_bottom_up(4) == 5

    # Test with n = 5
    assert solution.climbStairs_memoization(5) == 8
    assert solution.climbStairs_bottom_up(5) == 8

    # Test with n = 10
    assert solution.climbStairs_memoization(10) == 89
    assert solution.climbStairs_bottom_up(10) == 89

test_climbStairs()
print("All Test Cases Passed!")
