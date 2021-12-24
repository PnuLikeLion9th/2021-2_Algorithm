import sys

n, m = map(int, input().split())
S = {sys.stdin.readline().strip() for _ in range(n)}
cnt = 0
for _ in range(m):
    string = sys.stdin.readline().strip()
    if string in S:
        cnt += 1
print(cnt)