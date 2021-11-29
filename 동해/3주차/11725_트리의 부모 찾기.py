from collections import deque

def get_parents(root):
    res = [0] * (n+1)
    res[0] = 1
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if not res[child]:
                res[child] = node
                queue.append(child)
    return res

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
print(tree)

res = get_parents(1)
for i in res[2:]:
    print(i)