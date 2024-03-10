from sys import stdin

class Node(object):
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

tree = dict()

def preorder(node):
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
    
def inorder(node):
    if node.left != '.':
        preorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        preorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
    print(node.item, end='')

N = int(stdin.readline())

for _ in range(N):
    item, left, right = map(str, stdin.readline().rstrip().split())
    tree[item] = Node(item, left, right)
    
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
