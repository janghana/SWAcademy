from collections import deque
M, N = map(int, input().strip().split(' '))

tomato_matrix = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(M):
        if tomato_matrix[i][j] == 1:
            queue.append([i, j])
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and tomato_matrix[nx][ny] == 0:
                tomato_matrix[nx][ny] = tomato_matrix[x][y] + 1
                queue.append([nx, ny])
bfs()
result = 0
for i in tomato_matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)
