n = int(input())

# 피보나치 수열과 풀이 같음
# 1부터 시작
tile = []
for i in range(1, n+1):
    if i >= 3:
        tile.append(tile[i-2] + tile[i-3])
    else:
        tile.append(i)
print(tile[-1] % 10007)