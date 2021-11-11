n = int(input())
value = [0]*(n+1)
dp = [0]*(n+1)
for i in range(1,n+1):
    value[i] = int(input())
dp[1] = value[1]
if n>=2:
    dp[2] = value[1]+value[2]
    for i in range(3,n+1):
        dp[i] = max(dp[i-2]+value[i],dp[i-3]+value[i]+value[i-1],dp[i-1])
print(dp[n])
