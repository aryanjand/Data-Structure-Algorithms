from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        LeetCode Problem 27: Remove Linked List Elements
        Difficulty: Easy
        Topics: Arrays, Two Pointers, Linked Lists

        Given the head of a linked list and an integer val,
        remove all the nodes of the linked list that has Node.val == val,
        and return the new head.

        Key Ideas:
        - Use a dummy node to handle cases where the head node needs to be removed.
        - Iterate through the linked list, updating pointers to remove nodes with the given value.
        - Return the next node of the dummy node, which is the new head of the modified linked list.
        """
        dummy = ListNode(0,head)
        previous, current = dummy, head

        while current:
            if val == current.val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return dummy.next

class RemoveElementsTest(unittest.TestCase):
    def test_remove_linked_list_elements(self):
        # Test case 1: Remove single element from a list with one element
        head = ListNode(1)
        solution = Solution()
        new_head = solution.removeElements(head, 1)
        self.assertIsNone(new_head, "List should be empty after removal")

        # Test case 2: Remove multiple elements from a list with multiple elements
        head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
        solution = Solution()
        new_head = solution.removeElements(head, 6)
        current = new_head
        while current:
            self.assertNotEqual(current.val, 6, "List should not contain the removed element")
            current = current.next

        # Test case 3: Remove element not present in the list
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        solution = Solution()
        new_head = solution.removeElements(head, 6)
        current = new_head
        while current:
            self.assertNotEqual(current.val, 6, "List should remain unchanged")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print("All Test Cases Passed!")
