class Node:
    def __init__(self, n):
        self.left = None
        self.right = None
        self.value = n

def visit(node, path=[], queue=[]):
    if node:
        path.append(node.value)
        queue.append(node.left)
        queue.append(node.right)
        visit(queue.pop(0), path, queue)
    return path


n = Node(n=2)
n.left = Node(n=8)
n.right = Node(n=9)
n.left.left = Node(n=1)
n.left.right = Node(n=3)
n.right.left = Node(n=4)
n.right.right = Node(n=5)

print(visit(n))
