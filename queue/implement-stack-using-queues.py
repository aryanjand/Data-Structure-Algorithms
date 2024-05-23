import unittest
from collections import deque

class MyStack:
    """
        LeetCode Problem 225: Implement Stack using Queues
        Difficulty: Easy
        Topics: Stack, Design, Queue

        Implement a last-in-first-out (LIFO) stack using only two queues.
        The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

        Implement the MyStack class:

            void push(int x) Pushes element x to the top of the stack.
            int pop() Removes the element on the top of the stack and returns it.
            int top() Returns the element on the top of the stack.
            boolean empty() Returns true if the stack is empty, false otherwise.

        Key Ideas:
            - To implement a stack using a single queue, we can maintain the order of elements in the queue to simulate a stack.
            - When pushing an element, enqueue it to the queue.
            - When popping elements or accessing the top element, dequeue and enqueue elements until the last element is reached.
            - The last element in the queue will be the top element of the stack.
        """
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        n = len(self.q) - 2
        while n > 0:
            self.push(self.q.pop())
            n -= 1
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q

class TestMyStack(unittest.TestCase):
    def test_stack_operations(self):
        stack = MyStack()
        self.assertTrue(stack.empty())
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.top(), 2)
        self.assertFalse(stack.empty())
        stack.pop()
        stack.pop()
        self.assertTrue(stack.empty())
        # Test popping from an empty stack
        with self.assertRaises(IndexError):
            stack.pop()
        # Test top of an empty stack
        with self.assertRaises(IndexError):
            stack.top()

if __name__ == '__main__':
    unittest.main()
