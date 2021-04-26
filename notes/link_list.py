class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(node):
    result = node
    while result:
        print(result.val)
        result = result.next

node_a = ListNode(1)
last_node = ListNode(6)
node_a.next = ListNode(2)
node_a.next.next = ListNode(3)
node_a.next.next.next = ListNode(4)
node_a.next.next.next.next = ListNode(5)
node_a.next.next.next.next.next = last_node


def reverse(node):
    pre = None
    post = node
    while node:
        post = node.next
        node.next = pre
        pre = node
        node = post

print_list(node_a)
reverse(node_a)
print_list(last_node)
