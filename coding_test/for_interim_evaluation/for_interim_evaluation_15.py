T = int(input())

for _ in range(T):
    N, M, K = map(int ,input().split())
    cost_list = list(map(int ,input().split()))
    tmp = cost_list[K-1]
    nTrue = False
    index = 0
    for i in range(K,N):
        if cost_list[i] - tmp >= M:
            index = i
            nTrue = True
            break
    if nTrue:
        print(index + 1)
    else:
        print("JB")