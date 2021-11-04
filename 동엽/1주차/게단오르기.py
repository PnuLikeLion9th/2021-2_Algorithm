#철수는 계단을 오를 때 한번에 한계단 또는 두계단을 올라간다.
#만약 총 4계단을 오른다면 방법의 수는 1,1,1,1/ 1,1,2/ 1,2,1/ 2,1,1/ 2,2로 5가지이다
#계단이 n개일때 철수가 올라가는 총 방법의 수를 구하여라
#top-down(메모리제이션)
def dfs(len):
    if dp[len] >0:
        return dp[len]
    if len == 1 or len==2:
        return len
    else:
        dp[len] = dfs(len-1)+dfs(len-2)
        return dp[len]

n = int(input())
dp = [0]*(n+1)
print(dfs(n))