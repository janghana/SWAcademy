T = int(input())
def check_posit(x, y, N, M):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if jun_world[x][y] == "#":
        return False
    return True
for _ in range(T):
    N, M = map(int, input().split())
    jun_world = []
    for _ in range(N):
        jun_world.append(list(map(str, input())))
    K = int(input())
    K_input = input()

    prev = [0, 0]
    for i in range(N):
        for j in range(M):
            if jun_world[i][j] == '@':
                prev[0] = i
                prev[1] = j
                break
    for i in K_input:
        if i == 'R':
            if check_posit(prev[0], prev[1] + 1, N, M):
                prev[1] += 1
        elif i == 'L':
            if check_posit(prev[0], prev[1] - 1, N, M):
                prev[1] -= 1
        elif i == 'U':
            if check_posit(prev[0] - 1, prev[1], N, M):
                prev[0] -= 1
        elif i == 'D':
            if check_posit(prev[0] + 1, prev[1], N, M):
                prev[0] += 1
    print(prev[0]+1, prev[1]+1)
