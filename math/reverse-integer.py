import math

class Solution:
    def reverse(self, x: int) -> int:
        """
        Integer division by 10: Returns the quotient of the division, effectively removing the last digit(s) from the number.
        Modulo by 10: Returns the remainder of the division by 10, effectively extracting the last digit of the number.
        """

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            last_digit = int(math.fmod(x, 10))  # -1 %  10 = 9
            x = int(x / 10)  # -1 // 10 = -1

            if (res > MAX // 10 or (res == MAX // 10 and last_digit > MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and last_digit <= MIN % 10)):
                return 0

            res = (res * 10) + last_digit

        return res

    def reverse_2(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        is_negative = False

        if x < 0:
            is_negative = True
            x *= -1

        res = 0
        while x:
            last_digit = (x % 10)
            x = x // 10
            if (res > MAX // 10 or (res == MAX // 10 and last_digit > MAX % 10)):
                return 0
            res = (res * 10) + last_digit

        return res * -1 if is_negative else res

sol = Solution()
assert sol.reverse(123) == 321, "Test case 1 failed"
assert sol.reverse(-123) == -321, "Test case 2 failed"
assert sol.reverse(120) == 21, "Test case 3 failed"
assert sol.reverse(1534236469) == 0, "Test case 4 failed"
assert sol.reverse(-1563847412) == 0, "Test case 5 failed"
assert sol.reverse(0) == 0, "Test case 6 failed"

assert sol.reverse_2(123) == 321, "Test case 1 failed"
assert sol.reverse_2(-123) == -321, "Test case 2 failed"
assert sol.reverse_2(120) == 21, "Test case 3 failed"
assert sol.reverse_2(1534236469) == 0, "Test case 4 failed"
assert sol.reverse_2(-1563847412) == 0, "Test case 5 failed"
assert sol.reverse_2(0) == 0, "Test case 6 failed"

print("All Tests Passed!")
