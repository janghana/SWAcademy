N = int(input())
N_list = list(map(int, input().strip().split(' ')))
Q = int(input())
for i in range(Q):
    a, b = map(int, input().strip().split(' '))
    print(sum(N_list[a-1:b]))
