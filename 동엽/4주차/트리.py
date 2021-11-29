import sys
sys.setrecursionlimit(10**9)


n = int(input())
list = list(map(int,input().split()))
delnode = int(input())
cnt = 0
def dfs(start):#시작 노드(인덱스)
    global cnt
    check = False
    if start == delnode:
        return
    for node,parent in enumerate(list):
        if parent == start:#시작 노드를 부모 노드로 가지는 녀석
            check = True
            dfs(node)
    if check == False:
        cnt+=1
    return

if (list.index(-1) == delnode):
    print(cnt)
else:
    dfs(list.index(-1))
    if (list.count(list[delnode]) == 1):
        cnt+=1
    print(cnt)



