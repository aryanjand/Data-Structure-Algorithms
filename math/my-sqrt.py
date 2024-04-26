class Solution:
    def mySqrt_brute_force(self, x: int) -> int:

        for i in range(x):
            if x == 2:
                return 1
            elif i**2 > x:
                return i - 1
        return x

    def mySqrt_optimal(self, x: int) -> int:
        """
        The reason this works log(n) < sqrt(n)
        """
        res, left, right = 0, 0, x

        while left <= right:
            mid = (right - left) // 2 + left
            mid_squared = mid**2

            if mid_squared < x:
                left = mid + 1
                res = mid  # Save the value as a possible result.
                # This is because for values where the square is less than x, we update the left bound of the
                # search range and keep track of this mid value as a potential result.
                # For example, when finding the square root of 8, the loop will set res = 2 (mid = 2)
                # since the square of 2 is 4, which is less than 8, and we know the square root is between 2 and 3.
            elif mid_squared > x:
                right = mid - 1
            else:
                return mid
        return res



def test_mySqrt():
    solution = Solution()
    assert solution.mySqrt_brute_force(0) == 0
    assert solution.mySqrt_brute_force(1) == 1
    assert solution.mySqrt_brute_force(2) == 1
    assert solution.mySqrt_brute_force(3) == 1
    assert solution.mySqrt_brute_force(4) == 2
    assert solution.mySqrt_brute_force(8) == 2
    assert solution.mySqrt_brute_force(9) == 3
    assert solution.mySqrt_brute_force(16) == 4
    assert solution.mySqrt_brute_force(17) == 4
    assert solution.mySqrt_brute_force(2147395599) == 46339
    assert solution.mySqrt_optimal(0) == 0
    assert solution.mySqrt_optimal(1) == 1
    assert solution.mySqrt_optimal(2) == 1
    assert solution.mySqrt_optimal(3) == 1
    assert solution.mySqrt_optimal(4) == 2
    assert solution.mySqrt_optimal(8) == 2
    assert solution.mySqrt_optimal(9) == 3
    assert solution.mySqrt_optimal(16) == 4
    assert solution.mySqrt_optimal(17) == 4
    assert solution.mySqrt_optimal(2147395599) == 46339

test_mySqrt()
print("All Test Cases Passed!")
