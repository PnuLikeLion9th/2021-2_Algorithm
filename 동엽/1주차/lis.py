n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
dp=[0]*(n+1)
dp[1] = 1
res=0
for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dp[j]>max:
            max=dp[j]
    dp[i]=max+1
    if dp[i]>res:
        res=dp[i]
print(res)