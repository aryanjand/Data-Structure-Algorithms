from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head # Get's the second middle
        # fast, slow = head, head.next # Get's the first middle

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

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

def test_middleNode():
    solution = Solution()
    # Test with a linked list: 1 -> 2 -> 3 -> 4 -> 5
    original_list = create_linked_list([1, 2, 3, 4, 5])
    middle_node = solution.middleNode(original_list)
    assert middle_node.val == 3

    # Test with a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    original_list = create_linked_list([1, 2, 3, 4, 5, 6])
    middle_node = solution.middleNode(original_list)
    assert middle_node.val == 4

    # Test with a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    original_list = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    middle_node = solution.middleNode(original_list)
    assert middle_node.val == 4

    # Test with a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
    original_list = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    middle_node = solution.middleNode(original_list)
    assert middle_node.val == 5

    # Test with a linked list: 1 -> 2
    original_list = create_linked_list([1, 2])
    middle_node = solution.middleNode(original_list)
    assert middle_node.val == 2

    # Test with an empty linked list
    original_list = create_linked_list([])
    middle_node = solution.middleNode(original_list)
    assert middle_node == None

test_middleNode()
print("All Test Cases Passed!")
