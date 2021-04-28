# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head:
        return head
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    length = len(nodes)
    times = k % len(nodes)
    if times == 0:
        return head
    dummy = ListNode()
    for i in nodes[-times:] + [nodes[0]]:
        dummy.next = i
        dummy = i
    nodes[-times-1].next = None
    return nodes[-times]

def rotateRight_v2(head, k):
    if not head:
        return head
    length = 1
    last_node = head
    while True:
        if not last_node.next:
            break
        last_node = last_node.next
        length += 1
    last_node.next = head
    k = k % length
    temp_node = head
    for _ in range(length - k - 1):
        temp_node = temp_node.next
    result = temp_node.next
    temp_node.next = None
    return result

node_a = ListNode(1)
node_a.next = ListNode(2)
node_a.next.next = ListNode(3)
node_a.next.next.next = ListNode(4)
node_a.next.next.next.next = ListNode(5)
node_a.next.next.next.next.next = ListNode(6)

a = rotateRight_v2(node_a, 3)
while a:
    print(a.val)
    a = a.next

