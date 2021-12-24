n = int(input())
table = []
for i in range(n):
    t,p = map(int,input().split())
    table.append([t,p])

dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    if i+table[i][0]>n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],table[i][1]+dp[i+table[i][0]])

print(dp[0])
