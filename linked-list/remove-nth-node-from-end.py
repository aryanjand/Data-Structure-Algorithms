from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = current = head
        length = 0

        # Find the length of the linked list
        while current:
            length += 1
            current = current.next

        # If n exceeds the length of the linked list, do nothing and return head
        if n > length:
            return dummy.next

        # Calculate the position of the node to remove from the end
        length -= n
        current = dummy

        # Traverse to the node just before the one to remove
        while length > 0:
            length -= 1
            current = current.next

        # Remove the node by skipping over it
        current.next = current.next.next

        return dummy.next


def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head

def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

def test_removeNthFromEnd():
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        ([1], 1, []),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([], 1, []),
    ]

    for lst, n, expected_lst in test_cases:
        head = list_to_linked_list(lst)
        expected_head = list_to_linked_list(expected_lst)
        result = solution.removeNthFromEnd(head, n)
        assert linked_list_to_list(result) == linked_list_to_list(expected_head)

    print("All test cases pass")

test_removeNthFromEnd()
