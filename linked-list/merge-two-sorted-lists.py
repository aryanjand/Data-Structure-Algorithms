from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else: # avoid elif if not necessary
            # elif list1.val >= list2.val:
                current.next = list2
                list2 = list2.next

            current = current.next

        # avoid complicated if statements
        current.next = list1 or list2
        return dummy.next


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

def test_mergeTwoLists():
    solution = Solution()
    # Test with two sorted linked lists: 1 -> 2 -> 4 and 1 -> 3 -> 4
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged_list = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged_list) == [1, 1, 2, 3, 4, 4]

    # Test with an empty list and a non-empty list
    list1 = create_linked_list([])
    list2 = create_linked_list([1, 3, 5])
    merged_list = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged_list) == [1, 3, 5]

    # Test with two empty lists
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged_list = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged_list) == []

test_mergeTwoLists()
print("All Test Cases Passed!")
