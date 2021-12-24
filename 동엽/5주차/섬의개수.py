from collections import deque
dx = [1,-1,0,0,1,-1,-1,1]
dy = [0,0,1,-1,1,1,-1,-1]
while True:
    w,h = map(int,input().split())
    q = deque()
    cnt = 0
    if w == 0 and h==0:
        break
    board = [list(map(int,input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                board[i][j] = 0
                q.append([i,j])
                while q:
                    y,x = q.popleft()
                    for k in range(8):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0<= nx<w and 0<=ny<h and board[ny][nx]==1:
                            board[ny][nx] = 0
                            q.append((ny,nx))
                cnt+=1  
    print(cnt)




