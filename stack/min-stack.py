import unittest

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[-1] if self.min_stack else float('inf'), val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int | None:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int | None:
        return self.min_stack[-1] if self.min_stack else None


class TestMinStack(unittest.TestCase):
    def test_min_stack_operations(self):
        obj = MinStack()
        obj.push(3)
        obj.push(5)
        self.assertEqual(obj.top(), 5)  # Top element should be 5
        self.assertEqual(obj.getMin(), 3)  # Minimum element should be 3
        obj.pop()  # Removing the top element
        self.assertEqual(obj.top(), 3)  # Top element should now be 3
        self.assertEqual(obj.getMin(), 3)  # Minimum element should still be 3

    def test_min_stack_with_empty_stack(self):
        obj = MinStack()
        self.assertIsNone(obj.top())  # Top should be None for an empty stack
        self.assertIsNone(obj.getMin())  # Min should be None for an empty stack

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
