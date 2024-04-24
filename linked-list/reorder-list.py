# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Note it used 3 patterns,
    # 1. Fast Slow
    # 2. Reverse the list
    # 3. Merge the list
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return head

        # Get midpoint of the list
        slow, fast = head, head.next  # Fast starts from head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        second = slow.next  # second is the start of the second list
        prev = slow.next = None  # slow is now the end of the first half
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        # Merge the two lists
        first, second = head, prev
        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first, second = next1, next2  # Update pointers for the next iteration


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

def test_reorderList():
    solution = Solution()
    # Test with a linked list: 1 -> 2 -> 3 -> 4
    original_list = create_linked_list([1, 2, 3, 4])
    solution.reorderList(original_list)
    assert linked_list_to_list(original_list) == [1, 4, 2, 3]

    # Test with a linked list: 1 -> 2 -> 3 -> 4 -> 5
    original_list = create_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(original_list)
    assert linked_list_to_list(original_list) == [1, 5, 2, 4, 3]

    # Test with a linked list: 1
    original_list = create_linked_list([1])
    solution.reorderList(original_list)
    assert linked_list_to_list(original_list) == [1]

    # Test with an empty linked list
    original_list = create_linked_list([])
    solution.reorderList(original_list)
    assert linked_list_to_list(original_list) == []

test_reorderList()
print("All Test Cases Passed!")
