T = int(input())

for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    count = int(input())
    for i in range(count):
        U, V = map(int, input().split())
        N_list[U - 1] -= 1
        N_list[V - 1] += 1
    print(*N_list)
