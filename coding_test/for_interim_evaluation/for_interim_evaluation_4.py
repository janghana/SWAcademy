T = int(input())
for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    for i in N_list:
        for j in N_list[:]:
            if i <= j:
                continue
            if j not in N_list[N_list.index(i):]:
                continue
            del N_list[N_list.index(j, N_list.index(i),N)]
    print(*N_list)
