class ListNode:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.set = [ListNode() for i in range(10601 + 1)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        node = self.set[index]
        while node and node.next:
            if key == node.next.key:
                return
            node = node.next
        node.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        node = self.set[index]
        while node and node.next:
            if key == node.next.key:
                node.next = node.next.next
            node = node.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        node = self.set[index]
        while node and node.next:
            if key == node.next.key:
                return True
            node = node.next
        return False

def test_MyHashSet():
    hash_set = MyHashSet()
    hash_set.add(1)
    hash_set.add(2)
    assert hash_set.contains(1) == True
    assert hash_set.contains(3) == False
    hash_set.add(2)
    assert hash_set.contains(2) == True
    hash_set.remove(2)
    assert hash_set.contains(2) == False

test_MyHashSet()
print("All Test Cases Passed!")
