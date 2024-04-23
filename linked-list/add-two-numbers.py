from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            remainder = (l1_val + l2_val + carry) % 10 # Calculate the remainder of the sum of current digits and the carry
            carry = (l1_val + l2_val + carry) // 10 # Calculate the new carry for the next iteration
            current.next = ListNode(remainder)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

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

def test_addTwoNumbers():
    solution = Solution()
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8]

    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0]

    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

test_addTwoNumbers()
print("All Test Cases Passed!")
