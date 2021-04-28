class Node:
    def __init__(self, n):
        self.left = None
        self.right = None
        self.value = n

def level_order_visit(node, path=[], queue=[]):
    if node:
        path.append(node.value)
        queue.append(node.left)
        queue.append(node.right)
        level_order_visit(queue.pop(0), path, queue)
    return path

def preorder_visit(node, path=[]):
    if node:
        path.append(node.value)
        preorder_visit(node.left, path)
        preorder_visit(node.right, path)
    return path

def inorder_visit(node, path=[]):
    if node:
        inorder_visit(node.left, path)
        path.append(node.value)
        inorder_visit(node.right, path)
    return path

def postorder_visit(node, path=[]):
    if node:
        postorder_visit(node.left, path)
        postorder_visit(node.right, path)
        path.append(node.value)
    return path

#       2
#    8    9
#   1 3  4 5

n = Node(n=2)
n.left = Node(n=8)
n.right = Node(n=9)
n.left.left = Node(n=1)
n.left.right = Node(n=3)
n.right.left = Node(n=4)
n.right.right = Node(n=5)
print("origin tree:\n     2\n  8    9\n 1 3  4 5")
print(f"level order result: {level_order_visit(n)}")
print(f"pre-order result: {preorder_visit(n)}")
print(f"in-order result: {inorder_visit(n)}")
print(f"post-order result: {postorder_visit(n)}")
