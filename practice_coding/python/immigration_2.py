from sys import stdin

immigration_people, immigration_time = map(int, input().split())
arr = [int(stdin.readline()) for _ in range(immigration_people)]

lower, r = min(arr), max(arr) * immigration_time
ans = r

while lower <= r:
    total = 0
    mid = (lower + r) // 2

    for i in range(immigration_people):
        total += mid // arr[i]

    if total >= immigration_time:
        r = mid -1
        ans = min(mid, ans)

    else:
        lower = mid + 1

print(ans)