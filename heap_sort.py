import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        h = [(head.val, idx, head) for idx, head in enumerate(lists) if head is not None]
        heapq.heapify(h)
        dummy = ListNode()
        last = dummy
        while h:
            val, idx, node = heapq.heappop(h)
            last.next, last = node, node
            if last.next is not None:
                heapq.heappush(h, (last.next.val, idx, last.next))
        return dummy.next


node_a = ListNode(1)
node_a.next = ListNode(9)
node_a.next.next = ListNode(100)

node_b = ListNode(1)
node_b.next = ListNode(99)
node_b.next.next = ListNode(101)

node_c = ListNode(-50)
node_c.next = ListNode(0)
node_c.next.next = ListNode(3)

result = Solution().mergeKLists([node_a, node_b, node_c])
while result:
    print(result.val)
    result = result.next