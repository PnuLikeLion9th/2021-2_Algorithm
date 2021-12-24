from collections import deque
# 어렵다..
#크기가 같은 물고기 먹는거 무리무리 그러나 지나는 갈수있음
#지보다 작은 애는 먹을수있음
#가까운 물고기 여러마리면 가장 위 가장위 물고기 여러마리면 가장 왼쪽
n = int(input())
size = 2
dx = [1,-1,0,0]
dy = [0,0,1,-1]
sx,sy = 0,0
move_num = 0
eat = 0
board = [list(map(int,input().split())) for _ in range(n)]

def check_board(shark):
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and board[i][j] <shark:
                return True
    return False

def bfs(x,y):
    q,visited = deque([(x,y)]),set([(x,y)])
    time = 0
    flag = False

    while q:
        size = len(q)
