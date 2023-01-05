import math

T = int(input())
for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    index = N_list.index(min(N_list))
    while True:
        tmp = 0
        for i in range(index, N - 1):
            while N_list[i] > N_list[i + 1]:
                N_list[i] = math.floor(N_list[i] / 2)
                tmp = 1
        if tmp == 0:
            break
    index = N_list.index(min(N_list))
    if N_list[index] == 1:
        for i in range(index):
            N_list[i] = N_list[index]
    while True:
        tmp = 0
        for i in range(index):
            while N_list[i] > N_list[i + 1]:
                N_list[i] = math.floor(N_list[i] / 2)
                tmp = 1
        if tmp == 0:
            break

    print(*N_list)
