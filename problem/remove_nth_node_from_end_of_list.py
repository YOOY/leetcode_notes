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

def removeNthFromEnd_two_pointer(head, n):
    fast_node = head
    slow_node = head
    for _ in range(n+1):
        fast_node = fast_node.next
    while fast_node:
        fast_node = fast_node.next
        slow_node = slow_node.next
    slow_node.next = slow_node.next.next
    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

#print(removeNthFromEnd(head, 2))
print(removeNthFromEnd_two_pointer(head, 2))

while head:
    print(head.val)
    head = head.next