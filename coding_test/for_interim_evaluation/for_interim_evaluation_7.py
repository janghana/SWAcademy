N = int(input())
x_y_list = []
for _ in range(N):
    x_y_list.append(list(map(int,input().split())))
result = []
x_0, y_0 = x_y_list[0]
print(x_y_list)
for x,y in x_y_list[1:]:
    cnt = 0
    if x == x_0 and y != y_0:
        continue
    a = (y-y_0)/(x-x_0)
    b = y - (x * a)
    print(a,b)
    for x1,y1 in x_y_list:
        if y1 == a * x1 + b:
            cnt += 1
    result.append(cnt)
if len(result) == 0:
    print(1)
else:
    print(max(result))
