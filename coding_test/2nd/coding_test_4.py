A_list = list(map(int ,input().split()))
B_list = list(map(int ,input().split()))
A_dict = {}
B_dict = {}
result_add = []
result_sub = []

for i in range(0,len(A_list),2):
    A_dict[A_list[i+1]] = A_list[i]

for i in range(0,len(B_list),2):
    B_dict[B_list[i+1]] = B_list[i]

# for i in B_dict:
#     if i not in A_dict:
#         result_add.append(B_dict[i])
#         result_add.append(i)
#         result_sub.append(B_dict[i])
#         result_sub.append(i)
for i in A_dict:
    if i in B_dict:
        result_add.append(A_dict[i] + B_dict[i])
        result_add.append(i)
        if A_dict[i] == B_dict[i]:
            continue
        result_sub.append(A_dict[i] - B_dict[i])
        result_sub.append(i)
    elif i not in B_dict:
        result_add.append(A_dict[i])
        result_add.append(i)
        result_sub.append(A_dict[i])
        result_sub.append(i)

print(*result_add)
print(*result_sub)