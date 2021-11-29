k =int(input())
midorder = list(map(int,input().split()))
answer = [[] for _ in range(k)]
def dfs(list,layer):
    if len(list) == 1:
        answer[layer].append(list[0])
        return
    else:
        value = len(list)//2
        answer[layer].append(list[value])
        dfs(list[:value],layer+1)
        dfs(list[value+1:],layer+1)
        return
        
dfs(midorder,0)
for i in answer:
    for j in i:
        print(j,end=" ")
    print()