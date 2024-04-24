class Solution:
    def tribonacci(self, n: int) -> int:
        # Initialize the first three Tribonacci numbers
        t = [0, 1, 1]

        # Return the first three numbers directly
        if n < 3:
            return t[n]

        # Compute the next Tribonacci numbers using dynamic programming
        for i in range(3, n + 1):
            t[0], t[1], t[2] = t[1], t[2], sum(t) # Compute the sum of the last three numbers and save it to the last index

        # Return the last computed Tribonacci number
        return t[-1]



def test_tribonacci():
    solution = Solution()
    assert solution.tribonacci(0) == 0
    assert solution.tribonacci(1) == 1
    assert solution.tribonacci(2) == 1
    assert solution.tribonacci(3) == 2
    assert solution.tribonacci(4) == 4
    assert solution.tribonacci(5) == 7
    assert solution.tribonacci(6) == 13
    assert solution.tribonacci(7) == 24
    assert solution.tribonacci(8) == 44

test_tribonacci()
print("All Test Cases Passed!")
