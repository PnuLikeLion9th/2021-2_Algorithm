import sys

def getTree(values, depth):
    mid = (len(values)//2)     # 중간값 == root
    tree[depth].append(values[mid])
    if len(values) == 1:
        return
    getTree(values[:mid], depth+1)
    getTree(values[mid+1:], depth+1)
    
k = int(input())
values = list(map(int, sys.stdin.readline().strip().split()))
tree =[[] for _ in range(k)] 

getTree(values, 0)
for i in range(k):
    print(*tree[i])
    
    

