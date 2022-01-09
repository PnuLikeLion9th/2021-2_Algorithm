# 백준_14503_로봇 청소기_구현_골드 5

import sys
input = sys.stdin.readline

def dfs(a,b,d):
    global cnt
    if maps[a+dx[d]][b+dy[d]] == 0: # 현재 바라보는 방향에서 왼쪽좌표가 청소하지 않았을 때
        if d==0:
            maps[a+dx[d]][b+dy[d]] = -1
            cnt += 1
            dfs(a+dx[d], b+dy[d], 3)
        else:
            maps[a+dx[d]][b+dy[d]] = -1
            cnt += 1
            dfs(a+dx[d], b+dy[d], abs(1-d))
    else:
        flag = 0
        if d==0:
            for i in [3,2,1]: # 4 방향 돌면서 탐색
                if maps[a+dx[i]][b+dy[i]] == 0: 
                    flag = 1
                    maps[a+dx[i]][b+dy[i]] = -1
                    cnt += 1
                    dfs(a+dx[i], b+dy[i], i-1)
            if flag == 0: # 4 방향 전부 청소가 되어있거나 벽인 경우
                if maps[a+1][b] == -1: # 후진하는 영역이 벽이 아닌 경우
                    dfs(a+1, b, d)
                else: # 후진하는 영역이 벽일 경우
                    print(cnt)
                    exit(0)

        if d==1:
            for i in [0,3,2]:
                if maps[a+dx[i]][b+dy[i]] == 0: 
                    flag = 1
                    maps[a+dx[i]][b+dy[i]] = -1
                    cnt += 1
                    if i == 0:
                        dfs(a+dx[i], b+dy[i], 3)
                    else:
                        dfs(a+dx[i], b+dy[i], i-1)
            if flag == 0:
                if maps[a][b-1] == -1:
                    dfs(a, b-1, d)
                else:
                    print(cnt)
                    exit(0)
        if d==2:
            for i in [1,0,3]:
                if maps[a+dx[i]][b+dy[i]] == 0: 
                    flag = 1
                    maps[a+dx[i]][b+dy[i]] = -1
                    cnt += 1
                    if i == 0:
                        dfs(a+dx[i], b+dy[i], 3)
                    else:
                        dfs(a+dx[i], b+dy[i], i-1)
            if flag == 0:
                if maps[a-1][b] == -1:
                    dfs(a-1, b, d)
                else:
                    print(cnt)
                    exit(0)
        if d==3:
            for i in [2,1,0]:
                if maps[a+dx[i]][b+dy[i]] == 0: 
                    flag = 1
                    maps[a+dx[i]][b+dy[i]] = -1
                    cnt += 1
                    if i == 0:
                        dfs(a+dx[i], b+dy[i], 3)
                    else:
                        dfs(a+dx[i], b+dy[i], i-1)
            if flag == 0:
                if maps[a][b+1] == -1:
                    dfs(a, b+1, d)
                else:
                    print(cnt)
                    exit(0)

dx = [0,-1,0,1]
dy = [-1,0,1,0]

n,m = map(int,input().split())
r,c,d = map(int,input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))

cnt = 1
maps[r][c] = -1
dfs(r,c,d)