from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome_1(self, head: Optional[ListNode]) -> bool:
        """
        Time: O(N)
        Space: O(N)
        """
        array = []

        while head:
            array.append(head.val)
            head = head.next

        length = len(array)

        for i in range(length):
            if array[i] != array[length - i - 1]:
                return False

        return True


    def isPalindrome_2(self, head: Optional[ListNode]) -> bool:
        """
        Time: O(N)
        Space: O(1)
        """

        # how does this handle edge cases?
        if not head or not head.next:
            return True

        # Find middle of linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # how did getting the correct middle node work?
        # reverse the second half linked list
        prev, current = None, slow.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare the reversed second half with the first half
        # There was no need to cut the linked list in half.
        first_half, second_half = head, prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

def test_is_palindrome():
    def is_palindrome_test_case(arr, expected_output):
        head = create_linked_list(arr)
        sol = Solution()
        assert sol.isPalindrome_1(head) == expected_output, f"Expected {expected_output} for {arr}"
        assert sol.isPalindrome_2(head) == expected_output, f"Expected {expected_output} for {arr}"

    # Test cases
    is_palindrome_test_case([], True)  # Empty list
    is_palindrome_test_case([1], True)  # Single node list
    is_palindrome_test_case([1, 2, 2, 1], True)  # Palindrome with even length
    is_palindrome_test_case([1, 2, 3, 2, 1], True)  # Palindrome with odd length
    is_palindrome_test_case([1, 2, 3, 4, 5], False)  # Not a palindrome
    is_palindrome_test_case([1, 2, 3, 4], False)  # Non-palindrome with even length
    is_palindrome_test_case([1, 2, 3, 4, 5, 6, 7], False)  # Non-palindrome with odd length

    print("All test cases passed!")

# Define Solution class here...

test_is_palindrome()
