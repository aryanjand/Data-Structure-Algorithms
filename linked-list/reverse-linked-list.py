from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        # Traverse the original list
        while current:
            next = current.next  # Save the next node before changing the pointer
            current.next = previous  # Reverse the pointer to the previous node
            previous = current  # Move the previous pointer to the current node
            current = next  # Move the current pointer to the next node

        # Return the new head of the reversed list
        return previous

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

def test_reverseList():
    solution = Solution()
    # Test with a linked list: 1 -> 2 -> 3 -> 4 -> 5
    original_list = create_linked_list([1, 2, 3, 4, 5])
    reversed_list = solution.reverseList(original_list)
    assert linked_list_to_list(reversed_list) == [5, 4, 3, 2, 1]

    # Test with an empty linked list
    original_list = create_linked_list([])
    reversed_list = solution.reverseList(original_list)
    assert linked_list_to_list(reversed_list) == []

    # Test with a single-node linked list
    original_list = create_linked_list([1])
    reversed_list = solution.reverseList(original_list)
    assert linked_list_to_list(reversed_list) == [1]

test_reverseList()
print("All Test Cases Passed!")
