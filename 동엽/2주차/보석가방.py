# 최고 17kg의 무게를 저장 할 수 있는 가방이 있다. 그리고 각각 3kg,4kg,7kg,8kg,9kg의 무게를 가진 5종류의
# 보석이 있다. 이 보석들의 가치는 각각 4,5,10,11,13이다.
# 이 보석을 가방에 담는데 17kg을 넘지 않으면서 최대의 가치가 되도록 하려면 어떻게 담아야 할까?
# 각 종류별 보석의 개수는 무한이 많다. 한 종류의 보석을 여러 번 가방에 담을 수 있다는 뜻이다

#첫 번째 줄은 보석 종류의 개수와 가방에 담을 수 있는 무게의 한계값이 주어진다.
#두 번째 줄부터 각 보석의 무게와 가치가 주어진다.
#가방의 저장무게는 1000kg을 넘지 않는다. 보석의 개수는 30개 이내이다.
#가방에 담을 수 있는 보석의 최대가치를 출력하라.

n,m = map(int,input().split())

dp = [0]*(m+1)

for i in range(n):
    w,v = map(int,input().split())
    for j in range(w,m+1):
        dp[j]=max(dp[j],dp[j-w]+v)
print(dp[m])