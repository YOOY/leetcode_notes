# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    stack = []
    node = head
    while node:
        stack.append(node)
        node = node.next
    index = len(stack) - n
    if index != 0:
        stack[index-1].next = stack[index-1].next.next
    result = stack[0] if stack else None
    return result

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(removeNthFromEnd(head, 2))