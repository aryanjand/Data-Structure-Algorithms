import unittest

class MyQueue:
    """
    LeetCode Problem 232: Implement Queue using Stacks
    Difficulty: Easy
    Topics: Stack, Design, Queue

    Implement a first in first out (FIFO) queue using only two stacks.
    The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:

        void push(int x) Pushes element x to the back of the queue.
        int pop() Removes the element from the front of the queue and returns it.
        int peek() Returns the element at the front of the queue.
        boolean empty() Returns true if the queue is empty, false otherwise.

    Key Ideas:
    - To implement a queue using stacks, use two stacks: one for pushing elements and one for popping elements.
    - When pushing an element, simply push it to the "push stack."
    - When popping or peeking, check if the "pop stack" is empty. If it is, pop all elements from the "push stack" and push them onto the "pop stack."
    - The top element of the "pop stack" will then be the front element of the queue.
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not (self.s1 or self.s2)

class TestMyQueue(unittest.TestCase):
    def test_MyQueue(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertFalse(queue.empty())
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.peek(), 2)

        queue.push(4)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.pop(), 4)
        self.assertTrue(queue.empty())

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
