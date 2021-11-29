import sys
sys.setrecursionlimit(10**9)


n = int(input())
list = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    s,e = map(int,input().split())
    list[s].append(e)
    list[e].append(s)

def dfs(start,list,parent):
    for i in list[start]:
        if parent[i] ==0:
            parent[i] = start
            dfs(i,list,parent)

dfs(1,list,parent)

for i in range(2,n+1):
    print(parent[i])