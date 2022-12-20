from collections import deque

def bfs(graph, visited, i, j):
  q = deque()
  q.append((i, j))
  visited[i][j] = 1
  while q:
    x, y = q.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 1 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        q.append((nx, ny))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]  
while True:
  m, n = map(int, input().split())
  if m == 0 and n == 0:
    break
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))
  visited = [[0] * m for _ in range(n)]

  count = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1 and visited[i][j] == 0:
        bfs(graph, visited, i, j) 
        count += 1
  print(count)