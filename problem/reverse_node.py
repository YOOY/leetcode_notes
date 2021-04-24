# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = tmp = ListNode(0)
        first = True
        while head:
            a = []
            for i in range(k):
                a.append(head)
                head = head.next
                if not head:
                    break
            if len(a) == k:
                h,t = self.reverse(a)
            else:
                h,t = a[0], a[-1]
            if first:
                dummy.next = h
                first = False
            tmp.next = h
            tmp = t
        tmp.next = None
        return dummy.next

    def reverse(self, lists_of_node):
        head = tail = lists_of_node.pop()
        while lists_of_node:
            tail.next = lists_of_node.pop()
            tail = tail.next
        return head, tail

node_a = ListNode(1)
node_a.next = ListNode(2)
node_a.next.next = ListNode(3)
node_a.next.next.next = ListNode(4)
node_a.next.next.next.next = ListNode(5)
node_a.next.next.next.next.next = ListNode(6)

result = Solution().reverseKGroup(node_a, 4)
while result:
    print(result.val)
    result = result.next