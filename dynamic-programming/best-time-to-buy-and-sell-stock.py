from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = prices[0], prices[0], 0

        for stock in prices[1:]:
            if buy > stock:
                buy = min(buy, stock)
                sell = stock
            sell = max(sell, stock)
            profit = max(sell - buy, profit)
        return profit

def test_maxProfit():
    solution = Solution()
    # Test with a list of prices: [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    # Test with a list of prices: [7, 6, 4, 3, 1]
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0

    # Test with a list of prices: [2, 4, 1]
    assert solution.maxProfit([2, 4, 1]) == 2

    # Test with a list of prices: [3, 2, 6, 5, 0, 3]
    assert solution.maxProfit([3, 2, 6, 5, 0, 3]) == 4

    # Test with a list of prices: [2, 1, 2, 0, 1]
    assert solution.maxProfit([2, 1, 2, 0, 1]) == 1

test_maxProfit()
print("All Test Cases Passed!")
