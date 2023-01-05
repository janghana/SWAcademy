import math
T = int(input())

for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    check = True
    while check:
        tmp = 0
        for i in range(N-1):
            if N_list[i] > N_list[i+1]:
                N_list[i] = math.floor(N_list[i]/2)
                tmp = 1
        if tmp == 0:
            check = False
    print(*N_list)