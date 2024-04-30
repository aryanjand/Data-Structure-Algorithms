class Solution:
    def isValid(self, s: str) -> bool:
        parentheses, stack = {
            "(": ")",
            "{": "}",
            "[": "]"
        }, []

        for char in s:
            if char in parentheses.values():
                # if stack is not empty, then compare closeing parentheses.
                # if stack is empty return False
                if not stack or parentheses.get(stack.pop(), None) != char:
                    return False
            else:
                stack.append(char)

        return False if stack else True

def test_isValid():
    solution = Solution()

    # Test cases with valid parentheses
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("{[]}") == True

    # Test cases with invalid parentheses
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("{{{{}}}}}}") == False

    # Test case with an empty string
    assert solution.isValid("") == True

    # Test case with a single opening parenthesis
    assert solution.isValid("(") == False

    # Test case with a single closing parenthesis
    assert solution.isValid(")") == False

    print("All test cases pass")

test_isValid()
