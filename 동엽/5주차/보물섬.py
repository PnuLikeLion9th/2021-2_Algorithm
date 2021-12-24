from collections import deque

w,l = map(int,input().split())
board = [list(map(str,input()))for _ in range(w)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
q = deque()

def bfs(i,j):
    q.append([i,j])
    c = [[0]*l for _ in range(w)]
    c[i][j] = 1 
    num=0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k]+x
            ny = dy[k]+y
            if 0<=nx<w and 0<=ny<l and board[nx][ny] == "L" and c[nx][ny] == 0:
                c[nx][ny] = c[x][y]+1
                num = max(num, c[nx][ny])
                q.append([nx,ny])
    return num-1

cnt = 0
for i in range(w):
    for j in range(l):
        if board[i][j] == 'L':
            cnt = max(cnt,bfs(i,j))

print(cnt)


        
        

