N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(1, N):
    matrix[i][0] = min(matrix[i - 1][1], matrix[i - 1][2]) + matrix[i][0]
    matrix[i][1] = min(matrix[i - 1][0], matrix[i - 1][2]) + matrix[i][1]
    matrix[i][2] = min(matrix[i - 1][1], matrix[i - 1][0]) + matrix[i][2]
print(min(matrix[N - 1][0], matrix[N - 1][1], matrix[N - 1][2]))
