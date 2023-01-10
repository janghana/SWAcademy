K, N = map(int, input().strip().split(' '))
check_list = [False] * (N+1)
check_list[N] = True
cnt = 0
start = 0
mid = N // 2
for i in range(N):
    for i in range(start, mid):
        check_list[i] = True
    if start == mid:
        break
    cnt += 1
    start = mid
    mid = (mid + N) // 2
if N - K == 1:
    cnt += 1
print(cnt)