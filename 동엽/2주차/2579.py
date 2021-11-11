
#계단오르기
n= int(input())
stair = [0]*n
dp = [0]*n
for i in range(n):
    stair[i] = int(input())
dp[0] = stair[0]
if n>=2:
    dp[1] = stair[0]+stair[1]
    if n>=3:
        dp[2] = max(stair[0]+stair[2],stair[1]+stair[2])
        for i in range(3,n):
            dp[i] = max(dp[i-3]+stair[i-1]+stair[i],stair[i]+dp[i-2])

print(dp[n-1])