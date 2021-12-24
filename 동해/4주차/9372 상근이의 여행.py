import sys

N = int(input())

def dfs(root, cnt):
    visited[root] = 1
    for i in tree[root]:
        if visited[i] == 0:
            cnt = dfs(i, cnt+1)
    return cnt

for _ in range(N):
    n, m = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        tree[x].append(y)
        tree[y].append(x)
    visited = [0] * (n+1)
    print(dfs(1, 0))