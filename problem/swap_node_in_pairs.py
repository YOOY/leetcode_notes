# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head:
        return None
    dummy = ListNode()
    dummy.next = head
    dummy_head = dummy
    while dummy.next and dummy.next.next:
        first = dummy.next
        second = dummy.next.next
        first.next, second.next = second.next, first
        dummy.next = second
        dummy = dummy.next.next
    return dummy_head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

node = swapPairs(head)

while node:
    print(node.val)
    node = node.next