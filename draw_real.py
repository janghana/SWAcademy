import sys
row, col = map(int ,input().split())
i, j, color = map(str ,input().split())
i = int(i)
j = int(j)

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(matrix, x, y):
    queue = []
    queue.append((x, y))
    dx_dy_arr = []
    x_y_color = matrix[x][y]
    matrix[x][y] = color
    while queue:
        x, y = queue.pop()
        for k in range(0, 4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx and nx< row and 0<= ny and ny < col:
                if matrix[nx][ny] == x_y_color:
                    dx_dy_arr.append([nx,ny])
                    matrix[nx][ny] = "-"
                    queue.append((nx, ny))
    return dx_dy_arr

read = lambda: sys.stdin.readline().strip()
matrix = [list(map(str, list(read()))) for _ in range(row)]

dx_dy_arr = bfs(matrix, i, j)
for x, y in dx_dy_arr:
    matrix[x][y] = color

for i in matrix:
    print(''.join(i))