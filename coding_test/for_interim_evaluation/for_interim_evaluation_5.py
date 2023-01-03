T = int(input())
for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    max_ = 0
    result = []
    for i in N_list:
        if max_ <= i:
            max_ = i
            result.append(i)
    print(*result)
