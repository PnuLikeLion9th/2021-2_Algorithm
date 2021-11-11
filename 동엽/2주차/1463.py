#1로 만들기
n = int(input())
dp = [0]*(n+1)
if n>=2:
    dp[2] = 1
    for i in range(3,n+1):
        if i%6 == 0:
            dp[i] = min(dp[i//3]+1,dp[i//2]+1,dp[i-1]+1)
        elif i%3 == 0:
            dp[i] = min(dp[i//3]+1,dp[i-1]+1)
        elif i%2 == 0:
            dp[i] = min(dp[i//2]+1,dp[i-1]+1)
        else:
            dp[i] =dp[i-1]+1

print(dp[n])

#이게 더 깔끔한듯(좀더 dp스럽다)
for i in range(2,x+1):
    d[i] = d[i-1]+1
    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)