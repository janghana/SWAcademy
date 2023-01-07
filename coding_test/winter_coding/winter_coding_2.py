N = int(input())
x_y_list = []
for _ in range(N):
    x_y_list.append(list(map(int,input().split())))
result_dict = {}
x_0, y_0 = x_y_list[0]
for x, y in x_y_list:
    if x == x_0 and y == y_0:
        continue
    if x == x_0:
        if 0 not in result_dict:
            result_dict[0] = y
        else:
            result_dict[0].append(y)
        continue
    m = (y-y_0)/(x-x_0)
    b = y - (m * x)
    if m not in result_dict:
        result_dict[m] = [b]
    else:
        result_dict[m].append(b)
max_ = 0
for i in result_dict:
    if max_ < len(result_dict[i]):
        max_ = len(result_dict[i])
print(max_+1)

# N = int(input())
# x_y_list = []
# for _ in range(N):
#     x_y_list.append(list(map(int,input().split())))
# result = []
# x_0, y_0 = x_y_list[1]
# for x,y in x_y_list:
#     cnt = 0
#     if x != x_0:
#         a = (y-y_0)//(x-x_0)
#         b = y - (x * a)
#         if (y-y_0)/(x-x_0) != (y-y_0)//(x-x_0):
#             b += (y-y_0)/(x-x_0) - (y-y_0)//(x-x_0)
#         for x1,y1 in x_y_list:
#             if y1 == a * x1 + b:
#                 cnt += 1
#         result.append(cnt)
#     elif x == x_0:
#         for x1,y1 in x_y_list:
#             if y1 == y_0:
#                 cnt += 1
#         result.append(cnt)
# if len(result) == 0:
#     print(1)
# else:
#     print(max(result))
