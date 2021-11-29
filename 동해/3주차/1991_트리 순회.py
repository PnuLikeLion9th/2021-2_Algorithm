import sys

n = int(input())
tree = {}

# 트리 만들기
for _ in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

# 1) 전위 순회(root-> 왼 -> 오)
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 2) 중위 순회(왼 -> root -> 오)
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 3) 후위 순회(왼 -> 오 -> root)
def postorder(root):
    if root != '.':
        postorder(tree[root][0])        
        postorder(tree[root][1])
        print(root, end='')        
preorder('A')
print()
inorder('A')
print()
postorder('A')