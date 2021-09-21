from collections import deque
def bfs(x, y, point, maps):
    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    q = deque() q.append([x,y,point])
    while q:
        x, y, point = q.popleft()
        maps[x][y] = 0
        for dx, dy, in dir:
            nx, ny = x + dx, y + dy
            if nx == len(maps) - 1 and ny == len(maps[0])-1:
                return point +1
            elif 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 :
                maps[nx][ny] = 0 q.append([nx,ny,point+1])
    return -1
def solution(maps):
    return bfs(0,0,1,maps)

