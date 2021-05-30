class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    fast = slow = dummy = head
    while dummy:
        k -= 1
        if k == 0:
            fast = dummy
            break
        dummy = dummy.next
    dummy = fast
    while dummy.next:
        dummy = dummy.next
        slow = slow.next
    slow.val, fast.val = fast.val, slow.val

    return head

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)

r = swapNodes(h, 2)

while r:
    print(r.val)
    r = r.next